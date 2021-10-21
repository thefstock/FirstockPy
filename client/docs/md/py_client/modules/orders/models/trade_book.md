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

    `actid: str`
    :   Account Id of logged in user

    `uid: str`
    :   Logged in User Id

`TradeBookResponseModel(**data: Any)`
:   The response model for trade book endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `actid: Optional[str]`
    :   Account Id

    `avgprc: Optional[str]`
    :   Average trade price of total traded quantity

    `cstFrm: Optional[str]`
    :   Custom Firm

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange Segment

    `exchordid: Optional[str]`
    :   Exchange Order Number

    `fillshares: Optional[str]`
    :   Total Traded Quantity of this order

    `flid: Optional[str]`
    :   Fill ID

    `flprc: Optional[str]`
    :   Fill Price

    `flqty: Optional[str]`
    :   Fill Qty

    `fltm: Optional[str]`
    :   Fill Time

    `ls: Optional[str]`
    :   Lot size

    `norenordno: Optional[str]`
    :   Noren Order Number

    `ordersource: Optional[str]`
    :   Order Source

    `pp: Optional[str]`
    :   Price precision

    `prc: Optional[str]`
    :   Order Price

    `prctyp: Optional[py_client.common.enums.PriceType]`
    :   LMT / MKT Price type

    `prd: Optional[str]`
    :   Display product alias name, using prarr returned in user details.

    `qty: Optional[str]`
    :   Order Quantity

    `rejreason: Optional[str]`
    :   If order is rejected, reason in text form

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `ret: Optional[py_client.common.enums.RetentionType]`
    :   DAY / IOC / EOS Order validity

    `stat: py_client.common.enums.ResponseStatus`
    :   The trade book success or failure status

    `ti: Optional[str]`
    :   Tick size

    `token: Optional[str]`
    :   Token

    `trantype: Optional[py_client.common.enums.TransactionType]`
    :   B / S Transaction type of the order

    `tsym: Optional[str]`
    :   Trading symbol / contract on which order is placed.

    `uid: Optional[str]`
    :   User Id