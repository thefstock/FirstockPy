Module py_client.modules.orders.models.order_book
=================================================
Request and Response model for order book request

Classes
-------

`OrderBookRequestModel(**data: Any)`
:   The request model for order book  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   Logged in User Id

    `prd: Optional[str]`
    :   The product name

`OrderBookResponseModel(**data: Any)`
:   The response model for order book endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The order book success or failure status

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

    `status: Optional[str]`
    :   Order status

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

    `cancelqty: Optional[str]`
    :   Canceled quantity for order which is in status cancelled.

    `remarks: Optional[str]`
    :   Any message Entered during order entry.

    `dscqty: Optional[str]`
    :   Order disclosed quantity.

    `trgprc: Optional[str]`
    :   Order trigger price

    `ret: Optional[py_client.common.enums.RetentionType]`
    :   DAY / IOC / EOS Order validity

    `uid: Optional[str]`
    :   User Id

    `actid: Optional[str]`
    :   Account Id

    `bpprc: Optional[str]`
    :   Book Profit Price applicable only if product is selected as B (Bracket order )

    `blprc: Optional[str]`
    :   Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `trailprc: Optional[str]`
    :   Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `amo: Optional[str]`
    :   Yes / No

    `pp: Optional[str]`
    :   Price precision

    `ti: Optional[str]`
    :   Tick size

    `ls: Optional[str]`
    :   Lot size

    `token: Optional[str]`
    :   Contract Token

    `orddttm: Optional[str]`
    :   orddttm

    `ordenttm: Optional[str]`
    :   ordenttm

    `extm: Optional[str]`
    :   extm

    `snoordt: Optional[str]`
    :   0 for profit leg and 1 for stoploss leg

    `snonum: Optional[str]`
    :   This field will be present for product H and B; and only if it is profit/sl order.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration