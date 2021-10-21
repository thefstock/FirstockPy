Module py_client.modules.alerts.models.modify_alert
===================================================
Request and response models for modify alert request

Classes
-------

`ModifyAlertRequestModel(**data: Any)`
:   The request model for modify alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `ai_t: str`
    :   Alert Type

    `al_id: str`
    :   The id of the alert to modify

    `d: str`
    :   Data to be compared with LTP

    `exch: str`
    :   Exchange Segment

    `remarks: str`
    :   Any message Entered during order entry.

    `tsym: str`
    :   Trading symbol

    `uid: str`
    :   The user id of the login user

    `validity: py_client.common.enums.AlertValidity`
    :   DAY or GTT Validity

`ModifyAlertResponseModel(**data: Any)`
:   The response model for modify alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `al_id: str`
    :   The modified alert id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The modify alert success or failure status