Module py_client.modules.alerts.models.get_pending_gtt_order
============================================================
Request and response models for get pending gtt order request

Classes
-------

`GetPendingGttOrderRequestModel(**data: Any)`
:   The request model for get pending gtt order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

`GetPendingGttOrderResponseModel(**data: Any)`
:   The response model for get pending gtt order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `actid: Optional[str]`
    :   Login user account id

    `ai_t: Optional[str]`
    :   Alert Type

    `al_id: Optional[str]`
    :   Alert id

    `d: Optional[str]`
    :   Data to be compared with LTP

    `dscqty: Optional[str]`
    :   Disclosed quantity (Max 10% for NSE, and 50% for MCX)

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange Segment

    `prc: Optional[str]`
    :   Order price

    `prctyp: Optional[py_client.common.enums.PriceType]`
    :   Price type

    `prd: Optional[str]`
    :   The product name

    `qty: Optional[str]`
    :   Order quantity

    `remarks: Optional[str]`
    :   Any message Entered during order entry.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `ret: py_client.common.enums.RetentionType`
    :   Retention type

    `stat: py_client.common.enums.ResponseStatus`
    :   The get pending gtt order success or failure status

    `trantype: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type

    `tsym: Optional[str]`
    :   Trading symbol

    `validity: Optional[py_client.common.enums.AlertValidity]`
    :   DAY or GTT Validity