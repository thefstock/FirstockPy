Module py_client.modules.alerts.models.place_gtt_order
======================================================
Request and response models for place gtt order request

Classes
-------

`PlaceGttOrderRequestModel(**data: Any)`
:   The request model for place gtt order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Login user account id

    `ai_t: str`
    :   Alert Type

    `d: str`
    :   Data to be compared with LTP

    `dscqty: Optional[str]`
    :   Disclosed quantity (Max 10% for NSE, and 50% for MCX)

    `exch: str`
    :   Exchange Segment

    `prc: str`
    :   Order price

    `prctyp: py_client.common.enums.PriceType`
    :   Price type

    `prd: str`
    :   The product name

    `qty: str`
    :   Order quantity

    `remarks: str`
    :   Any message Entered during order entry.

    `ret: py_client.common.enums.RetentionType`
    :   Retention type

    `trantype: py_client.common.enums.TransactionType`
    :   Transaction type

    `tsym: str`
    :   Trading symbol

    `uid: str`
    :   The user id of the login user

    `validity: py_client.common.enums.AlertValidity`
    :   DAY or GTT Validity

`PlaceGttOrderResponseModel(**data: Any)`
:   The response model for place gtt order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `al_id: Optional[str]`
    :   Alert Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The place gtt order success or failure status