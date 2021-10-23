Module py_client.modules.alerts.models.get_pending_alert
========================================================
Request and response models for get pending alert request

Classes
-------

`GetPendingAlertRequestModel(**data: Any)`
:   The request model for get pending alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

`GetPendingAlertResponseModel(**data: Any)`
:   The response model for get pending alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get pending alert success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `al_id: Optional[str]`
    :   The id of the alert to modify

    `tsym: Optional[str]`
    :   Trading symbol

    `exch: Optional[str]`
    :   Exchange Segment

    `ai_t: Optional[str]`
    :   Alert Type

    `token: Optional[str]`
    :   Contract token

    `validity: py_client.common.enums.AlertValidity`
    :   DAY or GTT Validity

    `remarks: Optional[str]`
    :   Any message Entered during order entry.

    `d: Optional[str]`
    :   Data to be compared with LTP

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration