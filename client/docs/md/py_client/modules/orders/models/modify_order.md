Module py_client.modules.orders.models.modify_order
===================================================
Request and Response model for modify order request

Classes
-------

`ModifyOrderRequestModel(**data: Any)`
:   The request model for modify order  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   Logged in User Id

    `exch: str`
    :   Exchange

    `norenordno: str`
    :   Noren order number, which needs to be modified

    `tsym: str`
    :   Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)

    `qty: Optional[str]`
    :   Modified / New Quantity

    `prc: Optional[str]`
    :   Modified / New price

    `trgprc: Optional[str]`
    :   New trigger price in case of SL-MKT or SL-LMT

    `prctyp: Optional[py_client.common.enums.PriceType]`
    :   LMT / MKT / SLLMT / SL-MKT / DS / 2L / 3L

    `ret: Optional[py_client.common.enums.RetentionType]`
    :   New Retention type of the order.

    `bpprc: Optional[str]`
    :   Book Profit Price applicable only if product is selected as B (Bracket order )

    `blprc: Optional[str]`
    :   Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `trailprc: Optional[str]`
    :   Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )

`ModifyOrderResponseModel(**data: Any)`
:   The response model for modify order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The modify order success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `result: Optional[str]`
    :   Noren Order number of the order modified.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration