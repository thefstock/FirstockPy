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

    `uid: str`
    :   The user id of the login user

    `exch: Optional[str]`
    :   Exchange

`ExchMessageResponseModel(**data: Any)`
:   The response model for exch message endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The exch message success or failure status

    `request_time: Optional[datetime.datetime]`
    :   Response recieved time

    `exchmsg: Optional[str]`
    :   It will be present only on a successful response

    `exchtm: Optional[datetime.datetime]`
    :   Exchange Time

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration