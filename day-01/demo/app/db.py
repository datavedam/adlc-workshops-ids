"""SQLite storage for the mini hotel PMS.

One file, three tables: properties, reservations, folio_entries. Money
columns (reservations.nightly_rate, folio_entries.amount) are stored as TEXT
holding paisa-accurate decimal strings (e.g. "2450.75") so they never round
trip through a float. Callers convert to Decimal at the boundary — see
app/reservations.py for the pattern.

DB_PATH is a module-level variable, not a function default, so tests can
point it at a throwaway file (see tests/test_reservations.py).
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "hotel_pms.db"


def get_connection(db_path=None):
    """Return a sqlite3 connection with rows addressable by column name."""
    if db_path is None:
        db_path = DB_PATH
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path=None, seed=True):
    """Create the tables if they don't exist yet, and seed demo data.

    Seeding only happens if the properties table is empty, so this is safe
    to call more than once (e.g. once per test, or once at app start-up).
    """
    if db_path is None:
        db_path = DB_PATH

    conn = get_connection(db_path)
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS properties (
                property_id TEXT PRIMARY KEY,
                name TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS reservations (
                reservation_id TEXT PRIMARY KEY,
                property_id TEXT NOT NULL REFERENCES properties(property_id),
                guest_name TEXT NOT NULL,
                guest_email TEXT NOT NULL,
                room_number TEXT NOT NULL,
                nightly_rate TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'active'
            );

            CREATE TABLE IF NOT EXISTS folio_entries (
                entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                reservation_id TEXT NOT NULL REFERENCES reservations(reservation_id),
                entry_type TEXT NOT NULL,
                amount TEXT NOT NULL,
                description TEXT NOT NULL
            );
            """
        )
        conn.commit()

        already_seeded = conn.execute("SELECT COUNT(*) FROM properties").fetchone()[0] > 0
        if seed and not already_seeded:
            _seed(conn)
    finally:
        conn.close()


def _seed(conn):
    """Insert two properties, four reservations and their folio entries.

    RES-1001 and RES-1002 belong to PROP-A. RES-2001 and RES-2002 belong to
    PROP-B, so cross-property lookups (e.g. asking for RES-2001 as PROP-A)
    are easy to test.
    """
    conn.executemany(
        "INSERT INTO properties (property_id, name) VALUES (?, ?)",
        [
            ("PROP-A", "Datavedam Residency, Hyderabad"),
            ("PROP-B", "Datavedam Suites, Bengaluru"),
        ],
    )

    conn.executemany(
        "INSERT INTO reservations "
        "(reservation_id, property_id, guest_name, guest_email, room_number, nightly_rate, status) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            ("RES-1001", "PROP-A", "Asha Rao", "asha.rao@example.com", "101", "2500.00", "active"),
            ("RES-1002", "PROP-A", "Vikram Shah", "vikram.shah@example.com", "102", "2500.00", "active"),
            ("RES-2001", "PROP-B", "Meera Iyer", "meera.iyer@example.com", "201", "3100.25", "active"),
            ("RES-2002", "PROP-B", "Karan Mehta", "karan.mehta@example.com", "202", "3100.25", "active"),
        ],
    )

    conn.executemany(
        "INSERT INTO folio_entries (reservation_id, entry_type, amount, description) VALUES (?, ?, ?, ?)",
        [
            ("RES-1001", "charge", "5000.00", "Room charge - 2 nights"),
            ("RES-1001", "charge", "450.75", "Room service"),
            ("RES-1001", "payment", "3000.00", "Advance payment"),
            ("RES-1002", "charge", "2500.00", "Room charge - 1 night"),
            ("RES-2001", "charge", "6200.50", "Room charge - 2 nights"),
            ("RES-2001", "payment", "6200.50", "Full payment on checkout"),
            ("RES-2002", "charge", "3100.25", "Room charge - 1 night"),
            ("RES-2002", "payment", "1000.00", "Partial payment"),
        ],
    )

    conn.commit()
