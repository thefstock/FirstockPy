Module py_client.modules.alerts.models.set_alert
================================================
Request and response models for set alert request

Classes
-------

`SetAlertRequestModel(**data: Any)`
:   The request model for set alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `tsym: str`
    :   Trading symbol

    `exch: str`
    :   Exchange Segment

    `ai_t: str`
    :   Alert Type

    `validity: py_client.common.enums.AlertValidity`
    :   DAY or GTT Validity

    `remarks: str`
    :   Any message Entered during order entry.

    `d: str`
    :   Data to be compared with LTP

`SetAlertResponseModel(**data: Any)`
:   The response model for set alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The set alert success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `al_id: Optional[str]`
    :   Alert Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration