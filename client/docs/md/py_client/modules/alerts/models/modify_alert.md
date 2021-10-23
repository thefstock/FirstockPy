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

    `uid: str`
    :   The user id of the login user

    `al_id: str`
    :   The id of the alert to modify

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

`ModifyAlertResponseModel(**data: Any)`
:   The response model for modify alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The modify alert success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `al_id: str`
    :   The modified alert id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration