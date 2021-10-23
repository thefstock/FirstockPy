Module py_client.common.enums
=============================
Commonly used enumerators

Classes
-------

`RequestSourceType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   The source of the request, mobile or web

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `MOB`
    :

    `WEB`
    :

    `API`
    :

`ResponseStatus(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   The response success or failure status

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `OK`
    :

    `NOT_OK`
    :

`PriceType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   The price type for orders & trades

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `LIMIT`
    :

    `MARKET`
    :

    `STOP_LOSS_LIMIT`
    :

    `STOP_LOSS_MARKET`
    :

    `DS`
    :

    `SECOND_LEG`
    :

    `THIRD_LEG`
    :

`TransactionType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   The transaction type for orders & trades

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `BUY`
    :

    `SELL`
    :

`RestMethod(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   Enumeration for REST methods

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `GET`
    :

    `POST`
    :

    `PATCH`
    :

    `PUT`
    :

    `DELETE`
    :

    `OPTION`
    :

    `HEAD`
    :

`RetentionType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   The retention type for orders

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `DAY`
    :

    `IOC`
    :

    `EOS`
    :

`AlertValidity(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   The alert validity

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `DAY`
    :

    `GTT`
    :