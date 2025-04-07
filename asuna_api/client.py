from __future__ import annotations
from typing import TYPE_CHECKING

import aiohttp

from .http import HTTPClient
from .image import Image
from .errors import NotFound
from .enums import Endpoint

if TYPE_CHECKING:
    from ._types import EndpointResult, EndpointLiteral


class Client:
    """Represents the Asuna API client.

    This class is used to interact with the Asuna API and retrieve images.

    Parameters
    ----------
    session: aiohttp.ClientSession | None
        An optional aiohttp session to use for requests. If not provided, a new session will be created.
    """

    __slots__: str = "_http_client"

    def __init__(self, session: aiohttp.ClientSession | None = None) -> None:
        self._http_client = HTTPClient(session)

    async def get(self, name: EndpointLiteral | Endpoint) -> Image:
        """Get an image from the API.

        Parameters
        ----------
        name: EndpointLiteral | Endpoint
            The name of the image to retrieve. This can be a string or an Endpoint enum value.

        Returns
        -------
        Image
            The retrieved image object.
        """
        try:
            if isinstance(name, str):
                name = Endpoint(name.lower())

            response: EndpointResult = await self._http_client.get(name)  # type: ignore
        except (NotFound, ValueError):
            valid_options = [e.value for e in Endpoint]
            raise NotFound(
                f"{name!r} is not an option! Valid options are: {', '.join(valid_options)}"
            )

        return Image(self._http_client, response["url"], response["fileName"])

    async def close(self) -> None:
        """Closes the HTTP client session, if it was created by this client."""
        await self._http_client.close()
