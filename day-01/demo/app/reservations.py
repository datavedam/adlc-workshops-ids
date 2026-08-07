"""Reservation lookups.

This module is the pattern every other read in this codebase copies. It
shows all the house rules in one place:
  - the SQL filters by property_id AND reservation_id together, so a caller
    scoped to one property can never see, or even confirm the existence of,
    another property's reservation
  - a missing (or out-of-scope) record raises NotFoundError — it never
    returns None and never lets sqlite3 raise an unhandled exception
  - money is converted to Decimal from the stored string, never float
  - every lookup goes through the house logger, and only identifiers are
    logged — never the guest's name or email
"""
from decimal import Decimal

from app.db import get_connection
from app.errors import NotFoundError
from app.log import get_logger

logger = get_logger(__name__)


def get_reservation(property_id, reservation_id):
    """Return the reservation for property_id/reservation_id as a dict.

    Raises NotFoundError if no reservation with this id exists for this
    property. That includes the case where the reservation exists but
    belongs to a different property — the caller must get the same
    NotFoundError either way, not a hint that the id is "real".
    """
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT reservation_id, property_id, guest_name, guest_email, "
            "room_number, nightly_rate, status "
            "FROM reservations "
            "WHERE property_id = ? AND reservation_id = ?",
            (property_id, reservation_id),
        ).fetchone()
    finally:
        conn.close()

    if row is None:
        logger.info(
            "reservation not found property_id=%s reservation_id=%s",
            property_id,
            reservation_id,
        )
        raise NotFoundError(f"No reservation {reservation_id} for property {property_id}")

    logger.info(
        "reservation fetched property_id=%s reservation_id=%s",
        property_id,
        reservation_id,
    )

    return {
        "reservation_id": row["reservation_id"],
        "property_id": row["property_id"],
        "guest_name": row["guest_name"],
        "guest_email": row["guest_email"],
        "room_number": row["room_number"],
        "nightly_rate": Decimal(row["nightly_rate"]),
        "status": row["status"],
    }
