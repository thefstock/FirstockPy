Module py_client.modules.users
==============================
User Module
===========

This module contains the `datasource` and `models` required for user module.
This datasource is initialized inside the `client` and can be accessed by `client.users` property.

Usage
-----
```py
from py_client.modules.users import UserDataSource, LoginRequestModel

appstate = {}

users = new UserDataSource(base_url='https://yourapi.url/namespace/', state=appstate)

model = LoginRequestModel(...)
users.login(model)
```

Sub-modules
-----------
* py_client.modules.users.datasource
* py_client.modules.users.endpoints
* py_client.modules.users.models