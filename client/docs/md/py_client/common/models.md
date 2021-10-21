Module py_client.common.models
==============================
Common models used across the project

Classes
-------

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

`BankDetails(**data: Any)`
:   The bank details model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `acctnum: Optional[str]`
    :   Account Number

    `bankn: Optional[str]`
    :   Bank Name

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

    `prc: str`
    :   Order Price

    `prctyp: py_client.common.enums.PriceType`
    :   LMT / MKT / SL-LMT/ SL-MKT

    `prd: str`
    :   C / M / H Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call)

    `qty: str`
    :   Order Quantity

    `trantype: py_client.common.enums.TransactionType`
    :   BUY or SELL

    `trgprc: Optional[str]`
    :   Only to be sent in case of SL / SL-M order.

    `tsym: str`
    :   Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)

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

    `ls: Optional[float]`
    :   Lot size

    `pp: Optional[str]`
    :   Price precision

    `ti: Optional[float]`
    :   Tick size

    `token: Optional[str]`
    :   Token of the scrip (contract)

    `tsym: Optional[str]`
    :   Trading symbol of the scrip (contract)

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

`Product(**data: Any)`
:   The product model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `exch: List[str]`
    :   List of strings with enabled, allowed exchange names

    `prd: str`
    :   The product name

    `s_prdt_ali: str`
    :   The product display name

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

    `ls: Optional[float]`
    :   Lot size

    `pp: Optional[float]`
    :   Price precision

    `ti: Optional[float]`
    :   Tick size

    `token: Optional[str]`
    :   Token of the scrip (contract)

    `tsym: Optional[str]`
    :   Trading symbol of the scrip (contract)

`TBContract(**data: Any)`
:   Top/Bottom contract
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `c: Optional[str]`
    :   Previous Close price

    `lp: Optional[str]`
    :   LTP

    `oi: Optional[str]`
    :   Open interest

    `pc: Optional[str]`
    :   LTP percentage change

    `tsym: Optional[str]`
    :   Trading symbol

    `v: Optional[str]`
    :   volume

    `value: Optional[str]`
    :   Total traded value

`TradeDate(**data: Any)`
:   The trade date model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   The model config

    `trd_date: datetime.date`
    :