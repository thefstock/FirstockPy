Module py_client.modules.markets.models.get_option_chain
========================================================
Request and response models for get option chain request

Classes
-------

`GetOptionChainRequestModel(**data: Any)`
:   The request model for get option chain endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `tsym: str`
    :   Trading symbol of any of the option or future. Option chain for that underlying will be returned.
        (use url encoding to avoid special char error for symbols like M&M)

    `exch: str`
    :   Exchange

    `strprc: str`
    :   Mid price for option chain selection

    `cnt: str`
    :   Number of strike to return on one side of the mid price for PUT and CALL. 
        (example cnt is 4, total 16 contracts will be returned, if cnt is is 5 total 20 contract will be returned)

`GetOptionChainResponseModel(**data: Any)`
:   The response model for get option chain endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get option chain success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `values: Optional[List[py_client.modules.markets.models.get_option_chain.MarketOptionChain]]`
    :   List of items

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration

`MarketOptionChain(**data: Any)`
:   Market option chain
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `exch: Optional[str]`
    :   Exchange

    `tsym: Optional[str]`
    :   Trading symbol of the scrip (contract)

    `token: Optional[str]`
    :   Token of the scrip (contract)

    `optt: Optional[str]`
    :   Option Type

    `strprc: Optional[str]`
    :   Strike price

    `pp: Optional[str]`
    :   Price precision

    `ti: Optional[str]`
    :   Tick size

    `ls: Optional[str]`
    :   Lot size