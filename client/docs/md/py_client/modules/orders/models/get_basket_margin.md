Module py_client.modules.orders.models.get_basket_margin
========================================================
Request and Response model for get order margin request

Classes
-------

`GetBasketMarginRequestModel(**data: Any)`
:   The request model for get order margin  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   Logged in User Id

    `actid: str`
    :   Login users account ID

    `exch: str`
    :   Exchange (Select from ‘exarr’ Array provided in User Details response)

    `tsym: str`
    :   Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)

    `qty: str`
    :   Order Quantity

    `prc: str`
    :   Order Price

    `trgprc: Optional[str]`
    :   Only to be sent in case of SL / SL-M order.

    `prd: str`
    :   C / M / H Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call)

    `trantype: py_client.common.enums.TransactionType`
    :   BUY or SELL

    `prctyp: py_client.common.enums.PriceType`
    :   LMT / MKT / SLLMT / SL-MKT / DS / 2L / 3L

    `blprc: Optional[str]`
    :   Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )

    `rorgqty: Optional[str]`
    :   Optional field. Application only for modify order, open order quantity

    `fillshares: Optional[str]`
    :   Optional field. Application only for modify order, quantity already filled

    `rorgprc: Optional[str]`
    :   Optional field. Application only for modify order, open order price

    `orgtrgprc: Optional[str]`
    :   Optional field. Application only for modify order, open order trigger price

    `norenordno: Optional[str]`
    :   Optional field. Application only for H or B order modification

    `snonum: Optional[str]`
    :   Optional field. Application only for H or B order modification

    `basketlists: Optional[List[py_client.common.models.BasketList]]`
    :   Array of basketlist

`GetBasketMarginResponseModel(**data: Any)`
:   The response model for get order margin endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get basket margin success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `remarks: Optional[str]`
    :   This field will be available only on success.

    `marginused: Optional[str]`
    :   Total margin used.

    `marginusedtrade: Optional[str]`
    :   Margin used after trade.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration