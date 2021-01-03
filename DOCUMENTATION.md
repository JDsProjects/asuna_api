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
 
## Using the wrapper:
 
All available endpoints you can use.

### *await* client.get_gif(option)
---
Get a random funny gif.

**Available options:** "hug","kiss","neko","pat","slap","wholesome_foxes"

