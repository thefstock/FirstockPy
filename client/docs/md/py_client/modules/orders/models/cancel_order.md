Module py_client.modules.orders.models.cancel_order
===================================================
Request and Response model for cancel order request

Classes
-------

`CancelOrderRequestModel(**data: Any)`
:   The request model for cancel order  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `norenordno: str`
    :   Noren order number, which needs to be cancelled

    `uid: str`
    :   Logged in User Id

`CancelOrderResponseModel(**data: Any)`
:   The response model for cancel order endpoint
    
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

    `result: Optional[str]`
    :   Noren Order number of the order modified.

    `stat: py_client.common.enums.ResponseStatus`
    :   The cancel order success or failure status