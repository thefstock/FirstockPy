Module py_client.modules.orders.models.place_order
==================================================
Request and Response model for place order request

Classes
-------

`PlaceOrderRequestModel(**data: Any)`
:   The request model for place order request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Login users account ID

    `amo: Optional[str]`
    :   Yes , If not sent, of Not “Yes”, will be treated as Regular order.

    `blprc: Optional[str]`
    :   Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `bpprc: Optional[str]`
    :   Book Profit Price applicable only if product is selected as B (Bracket order )

    `dscqty: Optional[str]`
    :   Disclosed quantity (Max 10% for NSE, and 50% for MCX)

    `exch: str`
    :   Exchange (Select from ‘exarr’ Array provided in User Details response)

    `ordersource: Optional[str]`
    :   MOB / WEB / TT Used to generate exchange info fields.

    `prc: str`
    :   Order Price

    `prc2: Optional[str]`
    :   Price for second leg, mandatory for price type 2L and 3L

    `prc3: Optional[str]`
    :   Price for third leg, mandatory for price type 3L

    `prctyp: py_client.common.enums.PriceType`
    :   LMT / MKT / SLLMT / SL-MKT / DS / 2L / 3L

    `prd: str`
    :   C / M / H Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call)

    `qty: str`
    :   Order Quantity

    `qty2: Optional[str]`
    :   Quantity for second leg, mandatory for price type 2L and 3L

    `qty3: Optional[str]`
    :   Quantity for third leg, mandatory for price type 3L

    `ret: py_client.common.enums.RetentionType`
    :   DAY / EOS / IOC Retention type (Show options as per allowed exchanges) remarks Any tag by user to mark order.

    `trailprc: Optional[str]`
    :   Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `trantype: py_client.common.enums.TransactionType`
    :   B / S B -> BUY, S -> SELL

    `trantype2: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type of second leg, mandatory for price type 2L and 3L

    `trantype3: Optional[py_client.common.enums.TransactionType]`
    :   Transaction type of third leg, mandatory for price type 3L

    `trgprc: Optional[str]`
    :   Only to be sent in case of SL / SL-M order.

    `tsym: str`
    :   Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)

    `tsym2: Optional[str]`
    :   Trading symbol of second leg, mandatory for price type 2L and 3L (use url encoding to avoid special char error for symbols like M&M)

    `tsym3: Optional[str]`
    :   Trading symbol of third leg, mandatory for price type 3L (use url encoding to avoid special char error for symbols like M&M)

    `uid: str`
    :   Logged in User Id

`PlaceOrderResponseModel(**data: Any)`
:   The response model for place order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `emsg: Optional[str]`
    :   Error message if the request failed

    `norenordno: Optional[str]`
    :   It will be present only on successful Order placement to OMS.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The place order success or failure status