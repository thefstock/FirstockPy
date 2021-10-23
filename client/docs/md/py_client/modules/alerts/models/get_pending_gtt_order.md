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

    `stat: py_client.common.enums.ResponseStatus`
    :   The get pending gtt order success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `tsym: Optional[str]`
    :   Trading symbol

    `exch: Optional[str]`
    :   Exchange Segment

    `ai_t: Optional[str]`
    :   Alert Type

    `al_id: Optional[str]`
    :   Alert id

    `validity: Optional[py_client.common.enums.AlertValidity]`
    :   DAY or GTT Validity

    `remarks: Optional[str]`
    :   Any message Entered during order entry.

    `d: Optional[str]`
    :   Data to be compared with LTP

    `trantype: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type

    `prctyp: Optional[py_client.common.enums.PriceType]`
    :   Price type

    `prd: Optional[str]`
    :   The product name

    `ret: py_client.common.enums.RetentionType`
    :   Retention type

    `actid: Optional[str]`
    :   Login user account id

    `prc: Optional[str]`
    :   Order price

    `qty: Optional[str]`
    :   Order quantity

    `dscqty: Optional[str]`
    :   Disclosed quantity (Max 10% for NSE, and 50% for MCX)

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration