Module py_client.modules.orders.models.multileg_order_book
==========================================================
Request and Response model for multileg order book request

Classes
-------

`MultilegOrderBookRequestModel(**data: Any)`
:   The request model for multileg order book  request
    
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

`MultilegOrderBookResponseModel(**data: Any)`
:   The response model for multileg order book endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The multileg order book success or failure status

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

    `tsym2: Optional[str]`
    :   Trading symbol of second leg, mandatory for price type 2L and 3L

    `trantype2: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type of second leg, mandatory for price type 2L and 3L

    `qty2: Optional[str]`
    :   Quantity for second leg, mandatory for price type 2L and 3L

    `prc2: Optional[str]`
    :   Price for second leg, mandatory for price type 2L and 3L

    `tsym3: Optional[str]`
    :   Trading symbol of third leg, mandatory for price type 3L

    `trantype3: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type of third leg, mandatory for price type 3L

    `qty3: Optional[str]`
    :   Quantity for third leg, mandatory for price type 3L

    `prc3: Optional[str]`
    :   Price for third leg, mandatory for price type 3L

    `fillshares2: Optional[str]`
    :   Total Traded Quantity of 2nd Leg

    `avgprc2: Optional[str]`
    :   Average trade price of total traded quantity for 2nd leg

    `fillshares3: Optional[str]`
    :   Total Traded Quantity of 3rd Leg

    `avgprc3: Optional[str]`
    :   Average trade price of total traded quantity for 3rd leg

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration