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

    `prd: Optional[str]`
    :   The product name

    `uid: str`
    :   Logged in User Id

`OrderBookResponseModel(**data: Any)`
:   The response model for order book endpoint
    
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

    `amo: Optional[str]`
    :   Yes / No

    `avgprc: Optional[str]`
    :   Average trade price of total traded quantity

    `blprc: Optional[str]`
    :   Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `bpprc: Optional[str]`
    :   Book Profit Price applicable only if product is selected as B (Bracket order )

    `cancelqty: Optional[str]`
    :   Canceled quantity for order which is in status cancelled.

    `dscqty: Optional[str]`
    :   Order disclosed quantity.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange Segment

    `exchordid: Optional[str]`
    :   Exchange Order Number

    `extm: Optional[str]`
    :   extm

    `fillshares: Optional[str]`
    :   Total Traded Quantity of this order

    `ls: Optional[str]`
    :   Lot size

    `norenordno: Optional[str]`
    :   Noren Order Number

    `orddttm: Optional[str]`
    :   orddttm

    `ordenttm: Optional[str]`
    :   ordenttm

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

    `remarks: Optional[str]`
    :   Any message Entered during order entry.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `ret: Optional[py_client.common.enums.RetentionType]`
    :   DAY / IOC / EOS Order validity

    `snonum: Optional[str]`
    :   This field will be present for product H and B; and only if it is profit/sl order.

    `snoordt: Optional[str]`
    :   0 for profit leg and 1 for stoploss leg

    `stat: py_client.common.enums.ResponseStatus`
    :   The order book success or failure status

    `status: Optional[str]`
    :   Order status

    `ti: Optional[str]`
    :   Tick size

    `token: Optional[str]`
    :   Contract Token

    `trailprc: Optional[str]`
    :   Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `trantype: Optional[py_client.common.enums.TransactionType]`
    :   B / S Transaction type of the order

    `trgprc: Optional[str]`
    :   Order trigger price

    `tsym: Optional[str]`
    :   Trading symbol / contract on which order is placed.

    `uid: Optional[str]`
    :   User Id