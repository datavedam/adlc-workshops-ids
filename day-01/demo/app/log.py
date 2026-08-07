"""The house logger.

Every module in this codebase logs through get_logger(), not through print()
or logging.getLogger() directly, so the format stays consistent everywhere.

Guest names, emails, phone numbers, document numbers and card/payment data
must NEVER be logged, at any level. Log identifiers instead — property_id,
reservation_id, entry_id — never the personal data attached to them.
"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


def get_logger(name):
    """Return a logger configured with the house format."""
    return logging.getLogger(name)
