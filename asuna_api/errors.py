__all__ = ["AsunaError", "NotFound", "BadRequest", "Forbidden", "HTTPError"]


class AsunaError(Exception):
    """Base class for all Asuna-related exceptions."""

    pass


class NotFound(AsunaError):
    """Exception raised when a resource is not found."""

    pass


class BadRequest(AsunaError):
    """Exception raised for bad requests."""

    pass


class Forbidden(AsunaError):
    """Exception raised when access is forbidden."""

    pass


class HTTPError(AsunaError):
    """Exception raised for HTTP errors."""

    def __init__(self, status: int, content: str) -> None:
        super().__init__(f"HTTP Error {status}: {content}")
