Module py_client.modules.orders.models.exit_sno_order
=====================================================
Request and Response model for exit sno order request

Classes
-------

`ExitSnoOrderRequestModel(**data: Any)`
:   The request model for exit sno order  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `norenordno: str`
    :   Noren order number, which needs to be cancelled

    `prd: str`
    :   Allowed for only H and B products (Cover order and bracket order)

    `uid: str`
    :   Logged in User Id

`ExitSnoOrderResponseModel(**data: Any)`
:   The response model for exit sno order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `dmsg: Optional[str]`
    :   Display message, (will be present only in case of success).

    `emsg: Optional[str]`
    :   Error message if the request failed

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The exit sno success or failure status