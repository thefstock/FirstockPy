Module py_client.modules.orders.models.convert_product
======================================================
Request and Response model for product conversion request

Classes
-------

`ConvertProductRequestModel(**data: Any)`
:   The request model for product conversion request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Account id

    `ordersource: Optional[str]`
    :   MOB For Logging

    `postype: str`
    :   Day / CF Converting Day or Carry forward position

    `prd: str`
    :   Product to which the user wants to convert position.

    `prevprd: str`
    :   Original product of the position.

    `qty: float`
    :   Quantity to be converted.

    `trantype: py_client.common.enums.TransactionType`
    :   Transaction type

    `tsym: str`
    :   Unique id of contract on which order was placed.
        Can’t be modified, must be the same as that of original order.
        (use url encoding to avoid special char error for symbols like M&M)

    `uid: str`
    :   User id of the logged in user.

`ConvertProductResponseModel(**data: Any)`
:   The response model for product conversion endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `emsg: Optional[str]`
    :   Error message if the request failed

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The product conversion success or failure status