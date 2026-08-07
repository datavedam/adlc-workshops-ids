"""Tests for app/reservations.py — the pattern every new read in this
codebase should follow, including the cross-property isolation case.

Each test runs against a fresh throwaway sqlite file so tests never touch
each other's data or the developer's local hotel_pms.db.
"""
import os
import tempfile
import unittest
from decimal import Decimal

from app import db
from app.errors import NotFoundError
from app.reservations import get_reservation


class GetReservationTests(unittest.TestCase):
    def setUp(self):
        fd, path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        os.remove(path)  # init_db creates the file fresh
        self.db_path = path
        self._original_db_path = db.DB_PATH
        db.DB_PATH = path
        db.init_db()

    def tearDown(self):
        db.DB_PATH = self._original_db_path
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_get_reservation_returns_expected_fields(self):
        reservation = get_reservation("PROP-A", "RES-1001")

        self.assertEqual(reservation["reservation_id"], "RES-1001")
        self.assertEqual(reservation["property_id"], "PROP-A")
        self.assertEqual(reservation["guest_name"], "Asha Rao")
        self.assertEqual(reservation["status"], "active")
        self.assertIsInstance(reservation["nightly_rate"], Decimal)
        self.assertEqual(reservation["nightly_rate"], Decimal("2500.00"))

    def test_unknown_reservation_raises_not_found(self):
        with self.assertRaises(NotFoundError):
            get_reservation("PROP-A", "RES-9999")

    def test_cross_property_lookup_raises_not_found(self):
        # RES-2001 exists, but it belongs to PROP-B. A caller scoped to
        # PROP-A must not be able to fetch it — same error as "unknown".
        with self.assertRaises(NotFoundError):
            get_reservation("PROP-A", "RES-2001")

    def test_reservation_is_visible_to_its_own_property(self):
        # Sanity check for the case above: RES-2001 works fine under PROP-B.
        reservation = get_reservation("PROP-B", "RES-2001")
        self.assertEqual(reservation["reservation_id"], "RES-2001")


if __name__ == "__main__":
    unittest.main()
