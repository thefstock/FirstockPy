Module py_client.modules.markets.models.exch_message
====================================================
Request and response models for exch message request

Classes
-------

`ExchMessageRequestModel(**data: Any)`
:   The request model for exch message endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `exch: Optional[str]`
    :   Exchange

    `uid: str`
    :   The user id of the login user

`ExchMessageResponseModel(**data: Any)`
:   The response model for exch message endpoint
    
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

    `exchmsg: Optional[str]`
    :   It will be present only on a successful response

    `exchtm: Optional[datetime.datetime]`
    :   Exchange Time

    `request_time: Optional[datetime.datetime]`
    :   Response recieved time

    `stat: py_client.common.enums.ResponseStatus`
    :   The exch message success or failure status