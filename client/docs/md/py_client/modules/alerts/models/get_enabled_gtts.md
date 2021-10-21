Module py_client.modules.alerts.models.get_enabled_gtts
=======================================================
Request and response models for get enabled gtts request

Classes
-------

`GetEnabledGttsRequestModel(**data: Any)`
:   The request model for get enabled gtts endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

`GetEnabledGttsResponseModel(**data: Any)`
:   The response model for get enabled gtts endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `ai_ts: Optional[List[py_client.common.models.AlertType]]`
    :   List of alert types

    `emsg: Optional[str]`
    :   Error message if the request failed

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The get enabled gtts success or failure status