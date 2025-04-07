from typing import Literal, TypedDict

EndpointLiteral = Literal["hug", "kiss", "neko", "pat", "slap", "wholesome_foxes"]


class Endpoint(TypedDict):
    url: str
    imageCount: int


class Base(TypedDict):
    allEndpoints: list[str]
    endpointInfo: dict[EndpointLiteral, Endpoint]
    totalImages: int


class EndpointResult(TypedDict):
    fileName: str
    url: str
