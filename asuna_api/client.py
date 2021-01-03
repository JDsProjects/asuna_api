import aiohttp
from .http import HTTPClient
from yarl import URL
from .image import Image 
import datetime
from .minecraft import Minecraft

class InputError(Exception):
  __slots__ = ()
  pass

class InvalidUser(Exception):
  __slots__ = ()
  pass

class Client:
  __slots__ = ("_http_client")
   
  def __init__(self,session: aiohttp.ClientSession = None):
    self._http_client = HTTPClient(session)

  def asuna_api_url(self,endpoint):
    url = URL.build(scheme="https", host= "asuna.ga/api", path="/"+endpoint.lstrip("/"))
    return str(url)

  async def get_gif(self,name):
    options = ("hug","kiss","neko","pat","slap","wholesome_foxes")
    if not name.lower() in options:
      raise InputError(name + " is not a valid option!")
      
    response = await self._http_client.get(self.asuna_api_url(name))
    url = response.get("url")
    return Image(self._http_client, url)
  
  async def mc_user(self,username=None):
    if username is None:
      raise InvalidUser(str(username) + " is not a valid option")
    response = await self._http_client.get(self.mchistory_username(username))

    if isinstance(response,dict):
      namehistory = await self._http_client.get(self.mchistory_uuid(response.get("id")))
      for x in namehistory:
        if "changedToAt" in x.keys():
          changed_at=datetime.datetime.utcfromtimestamp(int(x["changedToAt"])/1000).strftime('%Y-%m-%d')
          x["changedToAt"] = changed_at
        
        if not "changedToAt" in x.keys():
          x["changedToAt"] = "Original Name"
           
      mc_data = {"username":response["name"],"uuid":response["id"],"name_history":namehistory}
      return Minecraft(mc_data)

    if isinstance(response,bytes):
      raise InvalidUser(username + " is not a valid option")

  def mchistory_username(self,username):
    url = URL.build(scheme="https",host="api.mojang.com/users/profiles/minecraft",path="/"+username.lstrip("/"))
    return str(url)
  
  def mchistory_uuid(self,uuid):
    url = URL.build(scheme="https",host="api.mojang.com/user/profiles",path="/"+uuid+"/names")
    return str(url)

  async def close(self):
    await self._http_client.close()
