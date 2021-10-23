Module py_client.common.models
==============================
Common models used across the project

Classes
-------

`Product(**data: Any)`
:   The product model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `prd: str`
    :   The product name

    `s_prdt_ali: str`
    :   The product display name

    `exch: List[str]`
    :   List of strings with enabled, allowed exchange names

`BankDetails(**data: Any)`
:   The bank details model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `bankn: Optional[str]`
    :   Bank Name

    `acctnum: Optional[str]`
    :   Account Number

`DpAccountNumber(**data: Any)`
:   The dp account number model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `dpnum: Optional[str]`
    :

`Scrip(**data: Any)`
:   The scrip model
    
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

    `pp: Optional[float]`
    :   Price precision

    `ti: Optional[float]`
    :   Tick size

    `ls: Optional[float]`
    :   Lot size

`BasketList(**data: Any)`
:   The basketlist model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

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
    :   LMT / MKT / SL-LMT/ SL-MKT

`IndexTokenPair(**data: Any)`
:   The basket criteria pair
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `idxname: str`
    :   The index name

    `token: str`
    :   Index token used to subscribe

`BasketCriteriaPair(**data: Any)`
:   The basket criteria pair
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `bskt: str`
    :   The basket name

    `crt: str`
    :   The criteria

`TBContract(**data: Any)`
:   Top/Bottom contract
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `tsym: Optional[str]`
    :   Trading symbol

    `lp: Optional[str]`
    :   LTP

    `c: Optional[str]`
    :   Previous Close price

    `v: Optional[str]`
    :   volume

    `value: Optional[str]`
    :   Total traded value

    `oi: Optional[str]`
    :   Open interest

    `pc: Optional[str]`
    :   LTP percentage change

`AlertType(**data: Any)`
:   The alert type model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `ai_t: str`
    :   Alert type

`TradeDate(**data: Any)`
:   The trade date model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `trd_date: datetime.date`
    :

    `Config`
    :   The model config

`ExchTsym(**data: Any)`
:   The exch_tsym model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `exch: Optional[str]`
    :   NSE, BSE, NFO ... Exchange

    `tsym: Optional[str]`
    :   Trading symbol of the scrip (contract)

    `token: Optional[str]`
    :   Token of the scrip (contract)

    `pp: Optional[str]`
    :   Price precision

    `ti: Optional[float]`
    :   Tick size

    `ls: Optional[float]`
    :   Lot size