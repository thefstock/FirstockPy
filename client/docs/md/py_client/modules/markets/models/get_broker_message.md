Module py_client.modules.markets.models.get_broker_message
==========================================================
Request and response models for get broker message request

Classes
-------

`GetBrokerMessageRequestModel(**data: Any)`
:   The request model for get broker message endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

`GetBrokerMessageResponseModel(**data: Any)`
:   The response model for get broker message endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get broker message success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `dmsg: Optional[str]`
    :   This will be present only in case of success

    `norentm: Optional[datetime.datetime]`
    :   Noren Time

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration