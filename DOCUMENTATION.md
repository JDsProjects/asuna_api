# Asuna_Api

Please Note Some of the source came from(with permission):
[Original Github](https://github.com/iDutchy/sr_api/)
Python wrapper for asuna.ga I am not the creator the asuna api, and some of this code came from the iDutchy some-random-api project so credits to them. Credits to iDutchy for the Original source.

For any questions and support for the wrapper, you can visit the Discord support server

# Getting Started:
To begin with, you'll have to install the package by doing one of the following commands:
- `pip install -U asuna-api`
- `python -m pip -U install asuna-api`

Or you can install directly from source by doing one of the following commands:
- `pip install -U git+https://github.com/JDJGInc/asuna_api`
- `python -m pip install -U git+https://github.com/JDJGInc/asuna_api`

After that, you will have to create the client:
```python
import asuna_api

client = asuna_api.Client() #Alternatively you can use your own aiohttp.ClientSession by passing session=yoursession to this
```
For future reference in this documentation: when referring to 'client' we refer to what has been defined above!

Also remember to await client.close() after you run your command(otherwise it may cause errors passing the session doesn't have this issue.)
 
## Using the wrapper:
 
All available endpoints you can use.

# *await* client.get_gif(option)
---
Get a random funny gif.

**Available options:** `"hug"`,`"kiss"`,`"neko"`,`"pat"`,`"slap"`,`"wholesome_foxes"`

**Parameters:**\
**- option** *(string)*: The type of gif you want.

**Return type:** [Image](https://github.com/JDJGInc/asuna_api/blob/master/DOCUMENTATION.md#image "Image object attributes") *(object)*

### *await* client.mc_user(username)
---
Get the username history and UUID from a minecraft user.

**Parameters:**\
**- username** *(string)*: Name of the minecraft user.

**Return type:** [MCuser](https://github.com/JDJGInc/asuna_api/blob/master/DOCUMENTATION.md#mcuser "MCuser object attributes") *(object)*

# *await client.random_history(number)*
---
Get a random response from [SP46's api](https://history.geist.ga/api/many?amount=1)

**Parameters:**\
**-number** *(string or int)*: Amount of random quotes(1-50), defaults to 1.

**Return type:** List

## Objects

Here is explained what attributes the returned objects have

### Image
---
The object returned from `client.get_gif()`

#### Image.url
The url of the image

### Image.filename
This returns the full name of the file, however only for apis that return it, otherwise it may return as None.

#### *await* Image.read()
This will return a bytes object from the image

#### *await* Image.save(filepath)
Locally save the image.\
**Note:** 'filepath' requires a *full* path! e.g. `/home/John/myimage.png`

### MCuser
---
The object returned from `client.mc_user()`

#### MCuser.name
Minecraft username

#### MCuser.uuid
The users UUID

#### MCuser.history
This will return a *list* of *dicts* with the users name history and date it was changed.

#### MCuser.formatted_history
A pre formatted list of the users name history

#### MCuser.reversed_formatted_history
A pre formatted list of the users name history in reversed order

Please note this is heavily based on the sra wrapper code the mcUser object itself is the exact same as that api however with TimeChangedAt added.
