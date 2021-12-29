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

    `prd: Optional[str]`
    :   The product name

    `uid: str`
    :   Logged in User Id

`MultilegOrderBookResponseModel(**data: Any)`
:   The response model for multileg order book endpoint
    
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

    `avgprc2: Optional[str]`
    :   Average trade price of total traded quantity for 2nd leg

    `avgprc3: Optional[str]`
    :   Average trade price of total traded quantity for 3rd leg

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

    `fillshares: Optional[str]`
    :   Total Traded Quantity of this order

    `fillshares2: Optional[str]`
    :   Total Traded Quantity of 2nd Leg

    `fillshares3: Optional[str]`
    :   Total Traded Quantity of 3rd Leg

    `ls: Optional[str]`
    :   Lot size

    `norenordno: Optional[str]`
    :   Noren Order Number

    `pp: Optional[str]`
    :   Price precision

    `prc: Optional[str]`
    :   Order Price

    `prc2: Optional[str]`
    :   Price for second leg, mandatory for price type 2L and 3L

    `prc3: Optional[str]`
    :   Price for third leg, mandatory for price type 3L

    `prctyp: Optional[py_client.common.enums.PriceType]`
    :   LMT / MKT Price type

    `prd: Optional[str]`
    :   Display product alias name, using prarr returned in user details.

    `qty: Optional[str]`
    :   Order Quantity

    `qty2: Optional[str]`
    :   Quantity for second leg, mandatory for price type 2L and 3L

    `qty3: Optional[str]`
    :   Quantity for third leg, mandatory for price type 3L

    `rejreason: Optional[str]`
    :   If order is rejected, reason in text form

    `remarks: Optional[str]`
    :   Any message Entered during order entry.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `ret: Optional[py_client.common.enums.RetentionType]`
    :   DAY / IOC / EOS Order validity

    `stat: py_client.common.enums.ResponseStatus`
    :   The multileg order book success or failure status

    `status: Optional[str]`
    :   Order status

    `ti: Optional[str]`
    :   Tick size

    `trailprc: Optional[str]`
    :   Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `trantype: Optional[py_client.common.enums.TransactionType]`
    :   B / S Transaction type of the order

    `trantype2: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type of second leg, mandatory for price type 2L and 3L

    `trantype3: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type of third leg, mandatory for price type 3L

    `trgprc: Optional[str]`
    :   Order trigger price

    `tsym: Optional[str]`
    :   Trading symbol / contract on which order is placed.

    `tsym2: Optional[str]`
    :   Trading symbol of second leg, mandatory for price type 2L and 3L

    `tsym3: Optional[str]`
    :   Trading symbol of third leg, mandatory for price type 3L

    `uid: Optional[str]`
    :   User Id