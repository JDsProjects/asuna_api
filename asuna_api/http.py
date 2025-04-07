from __future__ import annotations
from typing import TYPE_CHECKING, Any, ClassVar

import aiohttp

from .enums import Endpoint
from .errors import BadRequest, Forbidden, HTTPError, NotFound

if TYPE_CHECKING:
    from ._types import EndpointResult, Base


class HTTPClient:
    BASE_URL: ClassVar[str] = "https://asuna.ga/api"
    __slots__: tuple[str, ...] = ("_session", "_session_owner")

    def __init__(self, session: aiohttp.ClientSession | None = None) -> None:
        self._session: aiohttp.ClientSession | None = session
        self._session_owner: bool = session is None

    async def create_session(self) -> aiohttp.ClientSession:
        if self._session and not self._session.closed:
            return self._session

        self._session = aiohttp.ClientSession()
        return self._session

    async def get(
        self, url: str | Endpoint, **kwargs: Any
    ) -> Base | EndpointResult | bytes:
        session = await self.create_session()

        url = f"{self.BASE_URL}/{url.value}" if isinstance(url, Endpoint) else url
        async with session.get(url, **kwargs) as response:
            if response.status == 404:
                raise NotFound(f"Resource not found: {url}")
            elif response.status == 400:
                raise BadRequest(f"Bad request: {url}")
            elif response.status == 403:
                raise Forbidden(f"Access forbidden: {url}")
            elif response.status != 200:
                raise HTTPError(response.status, await response.text())

            try:
                content = await response.json()
            except aiohttp.ClientResponseError:
                content = await response.read()

            return content

    async def close(self) -> None:
        if self._session and self._session_owner and not self._session.closed:
            await self._session.close()
            self._session = None
