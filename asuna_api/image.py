from __future__ import annotations
from typing import TYPE_CHECKING

import io

if TYPE_CHECKING:
    from os import PathLike
    from .http import HTTPClient


class Image:
    """Represents an image from the API.

    This class is used to handle image data and save it to a file.
    It is initialized with a URL and a filename.

    Attributes
    ----------
    url: str
        The URL of the image.
    filename: str
        The filename of the image.
    """

    __slots__: tuple[str, ...] = ("url", "_http_client", "filename")

    def __init__(self, http_client: HTTPClient, /, url: str, filename: str) -> None:
        self.url: str = url
        self.filename: str = filename
        self._http_client: HTTPClient = http_client

    def __str__(self) -> str:
        return self.url if self.url is not None else ""

    def __repr__(self) -> str:
        return f"<Image filename={self.filename} url={self.url}>"

    async def read(self) -> bytes:
        """Reads the image data from the URL.

        Returns
        -------
        bytes
            The image data as bytes.
        """
        return await self._http_client.get(self.url)  # type: ignore

    async def save(
        self, fp: str | PathLike | io.IOBase, seek_start: bool = False
    ) -> None:
        """Saves the image data to a file or file-like object.

        Parameters
        ----------
        fp: str | PathLike | io.IOBase
            The file path or file-like object to save the image to.
        seek_start: bool
            Whether to seek to the start of the file-like object before writing. Defaults to False.

        Raises
        ------
        ValueError
            If a file-like object is provided but is not writable.
        OSError
            If the file path is invalid or the file cannot be opened.
        IOError
            If an I/O error occurs while writing to the file.
        """
        data: bytes = await self.read()  # type: ignore

        if isinstance(fp, io.IOBase):
            if not fp.writable():
                raise ValueError("The provided file-like object is not writable.")
            if seek_start:
                fp.seek(0)
            fp.write(data)
        else:
            with open(fp, "wb") as f:
                f.write(data)
