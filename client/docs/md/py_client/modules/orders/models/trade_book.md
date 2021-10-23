Module py_client.modules.orders.models.trade_book
=================================================
Request and Response model for trade book request

Classes
-------

`TradeBookRequestModel(**data: Any)`
:   The request model for trade book  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   Logged in User Id

    `actid: str`
    :   Account Id of logged in user

`TradeBookResponseModel(**data: Any)`
:   The response model for trade book endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The trade book success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `exch: Optional[str]`
    :   Exchange Segment

    `tsym: Optional[str]`
    :   Trading symbol / contract on which order is placed.

    `norenordno: Optional[str]`
    :   Noren Order Number

    `prc: Optional[str]`
    :   Order Price

    `qty: Optional[str]`
    :   Order Quantity

    `prd: Optional[str]`
    :   Display product alias name, using prarr returned in user details.

    `trantype: Optional[py_client.common.enums.TransactionType]`
    :   B / S Transaction type of the order

    `prctyp: Optional[py_client.common.enums.PriceType]`
    :   LMT / MKT Price type

    `fillshares: Optional[str]`
    :   Total Traded Quantity of this order

    `avgprc: Optional[str]`
    :   Average trade price of total traded quantity

    `rejreason: Optional[str]`
    :   If order is rejected, reason in text form

    `exchordid: Optional[str]`
    :   Exchange Order Number

    `ret: Optional[py_client.common.enums.RetentionType]`
    :   DAY / IOC / EOS Order validity

    `uid: Optional[str]`
    :   User Id

    `actid: Optional[str]`
    :   Account Id

    `pp: Optional[str]`
    :   Price precision

    `ti: Optional[str]`
    :   Tick size

    `ls: Optional[str]`
    :   Lot size

    `cstFrm: Optional[str]`
    :   Custom Firm

    `fltm: Optional[str]`
    :   Fill Time

    `flid: Optional[str]`
    :   Fill ID

    `flqty: Optional[str]`
    :   Fill Qty

    `flprc: Optional[str]`
    :   Fill Price

    `ordersource: Optional[str]`
    :   Order Source

    `token: Optional[str]`
    :   Token

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration