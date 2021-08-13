import aiohttp
from .http import HTTPClient
from yarl import URL
from .image import Image
import datetime
from .minecraft import Minecraft


class InputError(Exception):
    __slots__ = ()


class InvalidUser(Exception):
    __slots__ = ()


class Client:
    __slots__ = ("_http_client",)

    def __init__(self, session: aiohttp.ClientSession = None):
        self._http_client = HTTPClient(session)

    def asuna_api_url(self, endpoint):
        url = URL.build(
            scheme = "https", host = "asuna.ga/api", path="/" + endpoint.lstrip("/")
        )
        
        return str(url)

    def sp46_history(self, number):
        url = URL.build(
            scheme="https",
            host="history.geist.ga",
            path="/api/many",
            query={"amount": number},
        )

        return url

    async def random_history(self, number = None):
        if number is None:
            number = "1"
        if isinstance(number, int):
            number = str(number)
        if number.isdigit() is False:
            raise InputError(f"{number} is not a valid option!")

        if int(number) < 0 or int(number) > 51:
            raise InputError(number + " is not a valid option!")

        response = await self._http_client.get(self.sp46_history(number))
        results = response.get("results")
        return results

    async def get_gif(self, name):
        options = ("hug", "kiss", "neko", "pat", "slap", "wholesome_foxes")
        if not name.lower() in options:
            raise InputError(name + " is not a valid option!")

        response = await self._http_client.get(self.asuna_api_url(name))
        url = response.get("url")
        filename = response.get("fileName")
        return Image(self._http_client, url, filename)

    async def mc_user(self, username = None):
        if username is None:
            raise InvalidUser(str(username) + " is not a valid option")
            
        response = await self._http_client.get(self.mchistory_username(username))

        if isinstance(response, dict):
            api_response = await self._http_client.get(
              self.mchistory_uuid(response.get("id"))
            )

            for x in api_response:
                if "changedToAt" in x.keys():
                    x["timeChangedAt"] = datetime.datetime.utcfromtimestamp(
                        int(x["changedToAt"]) / 1000
                    )
                    
                    x["changedToAt"] = datetime.datetime.utcfromtimestamp(
                        int(x["changedToAt"]) / 1000
                    )

                if not "changedToAt" in x.keys():
                    x["changedToAt"] = "Original Name"

            mc_data = {
                "username": response["name"],
                "uuid": response["id"],
                "name_history": api_response,
            }
            
            return Minecraft(mc_data)

        if isinstance(response, bytes):
            raise InvalidUser(username + " is not a valid option")

    def mchistory_username(self, username):
        url = URL.build(
            scheme="https",
            host="api.mojang.com/users/profiles/minecraft",
            path="/" + username.lstrip("/"),
        )
        return str(url)

    def mchistory_uuid(self, uuid):
        url = URL.build(
            scheme="https",
            host="api.mojang.com/user/profiles",
            path="/" + uuid + "/names",
        )
        return str(url)

    async def close(self):
        await self._http_client.close()
