Module py_client.modules.alerts.models.modify_gtt_order
=======================================================
Request and response models for modify gtt order request

Classes
-------

`ModifyGttOrderRequestModel(**data: Any)`
:   The request model for modify gtt order endpoint
    
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
    :   Alert Type. should be original type can't be modified

    `validity: py_client.common.enums.AlertValidity`
    :   DAY or GTT Validity

    `remarks: str`
    :   Any message Entered during order entry.

    `d: str`
    :   Data to be compared with LTP

    `trantype: py_client.common.enums.TransactionType`
    :   Transaction type

    `prctyp: py_client.common.enums.PriceType`
    :   Price type

    `prd: str`
    :   The product name

    `ret: py_client.common.enums.RetentionType`
    :   Retention type

    `actid: str`
    :   Login user account id

    `prc: str`
    :   Order price

    `qty: str`
    :   Order quantity

    `dscqty: Optional[str]`
    :   Disclosed quantity (Max 10% for NSE, and 50% for MCX)

`ModifyGttOrderResponseModel(**data: Any)`
:   The response model for modify gtt order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: Union[py_client.common.enums.ResponseStatus, str]`
    :   The modify gtt order success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `al_id: Optional[str]`
    :   Alert Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration