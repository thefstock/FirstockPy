Module py_client.modules.orders.models.single_order_history
===========================================================
Request and Response model for single order history request

Classes
-------

`SingleOrderHistoryRequestModel(**data: Any)`
:   The request model for single order history  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `norenord: str`
    :   Noren Order Number

    `uid: str`
    :   Logged in User Id

`SingleOrderHistoryResponseModel(**data: Any)`
:   The response model for single order history endpoint
    
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

    `rpt: Optional[str]`
    :   Report Type (fill/complete etc)

    `stat: py_client.common.enums.ResponseStatus`
    :   The single order history success or failure status

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