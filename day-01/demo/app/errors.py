"""Domain errors for the mini PMS.

Map these at the edge of the app (an HTTP handler, a CLI, whatever calls in):
NotFoundError -> 404, ValidationError -> 400. Never let a missing record
fall through as an unhandled exception — that's how a "not found" becomes an
unintended 500.
"""


class NotFoundError(Exception):
    """Raised when a requested record does not exist for the caller's scope."""


class ValidationError(Exception):
    """Raised when caller-supplied input is malformed or out of range."""
