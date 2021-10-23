Module py_client.modules.watchlists.models.get_quotes
=====================================================
The request and response models for get quotes request

Classes
-------

`GetQuotesRequestModel(**data: Any)`
:   The request model for get quotes endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `exch: Optional[str]`
    :   Exchange

    `token: Optional[str]`
    :   Contract Token

`GetQuotesResponseModel(**data: Any)`
:   The response model for get quotes endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get scrips success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange

    `tsym: Optional[str]`
    :   Trading Symbol

    `cname: Optional[str]`
    :   Company Name

    `symnam: Optional[str]`
    :   Symbol Name

    `seg: Optional[str]`
    :   Segment

    `instname: Optional[str]`
    :   Intrument Name

    `isin: Optional[str]`
    :   ISIN

    `ti: Optional[float]`
    :   Tick Size

    `ls: Optional[float]`
    :   Lot Size

    `pp: Optional[float]`
    :   Price precision

    `mult: Optional[float]`
    :   Multiplier

    `token: Optional[str]`
    :   Contract Token

    `prcftr_d: Optional[str]`
    :   ((GN / GD) * (PN/PD))

    `uc: Optional[float]`
    :   Upper circuit limit

    `lc: Optional[float]`
    :   Lower circuit limit

    `lp: Optional[float]`
    :   LTP

    `h: Optional[float]`
    :   Day High Price

    `l: Optional[float]`
    :   Day Low Price

    `v: Optional[float]`
    :   Volume

    `ltq: Optional[float]`
    :   Last trade quantity

    `ltt: Optional[str]`
    :   Last trade time

    `bp1: Optional[float]`
    :   Best Buy Price

    `sp1: Optional[float]`
    :   Best Sell Price

    `bp2: Optional[float]`
    :   Best Buy Price

    `sp2: Optional[float]`
    :   Best Sell Price

    `bp3: Optional[float]`
    :   Best Buy Price

    `sp3: Optional[float]`
    :   Best Sell Price

    `bp4: Optional[float]`
    :   Best Buy Price

    `sp4: Optional[float]`
    :   Best Sell Price

    `bp5: Optional[float]`
    :   Best Buy Price

    `sp5: Optional[float]`
    :   Best Sell Price

    `bq1: Optional[float]`
    :   Best Buy Quantity

    `sq1: Optional[float]`
    :   Best Sell Quantity

    `bq2: Optional[float]`
    :   Best Buy Quantity

    `sq2: Optional[float]`
    :   Best Sell Quantity

    `bq3: Optional[float]`
    :   Best Buy Quantity

    `sq3: Optional[float]`
    :   Best Sell Quantity

    `bq4: Optional[float]`
    :   Best Buy Quantity

    `sq4: Optional[float]`
    :   Best Sell Quantity

    `bq5: Optional[float]`
    :   Best Buy Quantity

    `sq5: Optional[float]`
    :   Best Sell Quantity

    `bo1: Optional[float]`
    :   Best Buy Orders

    `so1: Optional[float]`
    :   Best Sell Orders

    `bo2: Optional[float]`
    :   Best Buy Orders

    `so2: Optional[float]`
    :   Best Sell Orders

    `bo3: Optional[float]`
    :   Best Buy Orders

    `so3: Optional[float]`
    :   Best Sell Orders

    `bo4: Optional[float]`
    :   Best Buy Orders

    `so4: Optional[float]`
    :   Best Sell Orders

    `bo5: Optional[float]`
    :   Best Buy Orders

    `so5: Optional[float]`
    :   Best Sell Orders

    `Config`
    :   model configuration