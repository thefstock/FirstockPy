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

    `exch: Optional[str]`
    :   Exchange

    `token: Optional[str]`
    :   Contract Token

    `uid: str`
    :   The user id of the login user

`GetQuotesResponseModel(**data: Any)`
:   The response model for get quotes endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `bo1: Optional[float]`
    :   Best Buy Orders

    `bo2: Optional[float]`
    :   Best Buy Orders

    `bo3: Optional[float]`
    :   Best Buy Orders

    `bo4: Optional[float]`
    :   Best Buy Orders

    `bo5: Optional[float]`
    :   Best Buy Orders

    `bp1: Optional[float]`
    :   Best Buy Price

    `bp2: Optional[float]`
    :   Best Buy Price

    `bp3: Optional[float]`
    :   Best Buy Price

    `bp4: Optional[float]`
    :   Best Buy Price

    `bp5: Optional[float]`
    :   Best Buy Price

    `bq1: Optional[float]`
    :   Best Buy Quantity

    `bq2: Optional[float]`
    :   Best Buy Quantity

    `bq3: Optional[float]`
    :   Best Buy Quantity

    `bq4: Optional[float]`
    :   Best Buy Quantity

    `bq5: Optional[float]`
    :   Best Buy Quantity

    `cname: Optional[str]`
    :   Company Name

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange

    `h: Optional[float]`
    :   Day High Price

    `instname: Optional[str]`
    :   Intrument Name

    `isin: Optional[str]`
    :   ISIN

    `l: Optional[float]`
    :   Day Low Price

    `lc: Optional[float]`
    :   Lower circuit limit

    `lp: Optional[float]`
    :   LTP

    `ls: Optional[float]`
    :   Lot Size

    `ltq: Optional[float]`
    :   Last trade quantity

    `ltt: Optional[str]`
    :   Last trade time

    `mult: Optional[float]`
    :   Multiplier

    `pp: Optional[float]`
    :   Price precision

    `prcftr_d: Optional[str]`
    :   ((GN / GD) * (PN/PD))

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `seg: Optional[str]`
    :   Segment

    `so1: Optional[float]`
    :   Best Sell Orders

    `so2: Optional[float]`
    :   Best Sell Orders

    `so3: Optional[float]`
    :   Best Sell Orders

    `so4: Optional[float]`
    :   Best Sell Orders

    `so5: Optional[float]`
    :   Best Sell Orders

    `sp1: Optional[float]`
    :   Best Sell Price

    `sp2: Optional[float]`
    :   Best Sell Price

    `sp3: Optional[float]`
    :   Best Sell Price

    `sp4: Optional[float]`
    :   Best Sell Price

    `sp5: Optional[float]`
    :   Best Sell Price

    `sq1: Optional[float]`
    :   Best Sell Quantity

    `sq2: Optional[float]`
    :   Best Sell Quantity

    `sq3: Optional[float]`
    :   Best Sell Quantity

    `sq4: Optional[float]`
    :   Best Sell Quantity

    `sq5: Optional[float]`
    :   Best Sell Quantity

    `stat: py_client.common.enums.ResponseStatus`
    :   The get scrips success or failure status

    `symnam: Optional[str]`
    :   Symbol Name

    `ti: Optional[float]`
    :   Tick Size

    `token: Optional[str]`
    :   Contract Token

    `tsym: Optional[str]`
    :   Trading Symbol

    `uc: Optional[float]`
    :   Upper circuit limit

    `v: Optional[float]`
    :   Volume