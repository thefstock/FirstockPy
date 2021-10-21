Module py_client.modules.holdings_limits.models.holdings
========================================================
Request and response models for holdings request

Classes
-------

`HoldingsRequestModel(**data: Any)`
:   The request model for holdings endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Account id of the logged in user.

    `prd: str`
    :   Product name

    `uid: str`
    :   The user id of the login user

`HoldingsResponseModel(**data: Any)`
:   The response model for holdings endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `benqty: Optional[float]`
    :   Beneficiary quantity

    `brkcolqty: Optional[float]`
    :   Broker Collateral

    `btstcolqty: Optional[float]`
    :   BTST Collateral quantity

    `btstqty: Optional[float]`
    :   BTST quantity

    `colqty: Optional[float]`
    :   Collateral quantity

    `dpqty: Optional[float]`
    :   DP Holding quantity

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch_tsym: Optional[List[py_client.common.models.ExchTsym]]`
    :   Array of objects exch_tsym objects as defined below.

    `holdqty: Optional[float]`
    :   Holding quantity

    `npoadqty: Optional[float]`
    :   Non Poa display quantity

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The holdings success or failure status

    `unplgdqty: Optional[float]`
    :   Unpledged quantity

    `upldprc: Optional[float]`
    :   Average price uploaded along with holdings

    `usedqty: Optional[float]`
    :   Holding used today