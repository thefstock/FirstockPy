Module py_client.modules.holdings_limits.models.limits
======================================================
Request and response models for limits request

Classes
-------

`LimitsRequestModel(**data: Any)`
:   The request model for limits endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Account id of the logged in user.

    `exch: Optional[str]`
    :   Exchange

    `prd: Optional[str]`
    :   Product name

    `seg: Optional[str]`
    :   CM / FO / FX - Segment

    `uid: str`
    :   The user id of the login user

`LimitsResponseModel(**data: Any)`
:   The response model for limits endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `actid: Optional[str]`
    :   Account id of the logged in user.

    `addscripbskmrg: Optional[str]`
    :   Additional scrip basket margin

    `addscripbskmrg_c_i: Optional[str]`
    :   Additional scrip basket margin (Commodity Intraday)

    `addscripbskmrg_c_m: Optional[str]`
    :   Additional scrip basket margin (Commodity Margin)

    `addscripbskmrg_d_i: Optional[str]`
    :   Additional scrip basket margin (Derivative Intraday)

    `addscripbskmrg_d_m: Optional[str]`
    :   Additional scrip basket margin (Derivative Margin)

    `addscripbskmrg_f_i: Optional[str]`
    :   Additional scrip basket margin (FX Intraday)

    `addscripbskmrg_f_m: Optional[str]`
    :   Additional scrip basket margin (FX Margin)

    `brkage_c_b: Optional[str]`
    :   Brokerage (Commodity Bracket Order)

    `brkage_c_h: Optional[str]`
    :   Brokerage (Commodity High Leverage)

    `brkage_c_i: Optional[str]`
    :   Brokerage (Commodity Intraday)

    `brkage_c_m: Optional[str]`
    :   Brokerage (Commodity Margin)

    `brkage_d_b: Optional[str]`
    :   Brokerage (Derivative Bracket Order)

    `brkage_d_h: Optional[str]`
    :   Brokerage (Derivative High Leverage)

    `brkage_d_i: Optional[str]`
    :   Brokerage (Derivative Intraday)

    `brkage_d_m: Optional[str]`
    :   Brokerage (Derivative Margin)

    `brkage_e_b: Optional[str]`
    :   Brokerage (Equity Bracket Order)

    `brkage_e_c: Optional[str]`
    :   Brokerage (Equity CAC)

    `brkage_e_h: Optional[str]`
    :   Brokerage (Equity High Leverage)

    `brkage_e_i: Optional[str]`
    :   Brokerage (Equity Intraday)

    `brkage_e_m: Optional[str]`
    :   Brokerage (Equity Margin)

    `brkage_f_b: Optional[str]`
    :   Brokerage (FX Bracket Order)

    `brkage_f_h: Optional[str]`
    :   Brokerage (FX High Leverage)

    `brkage_f_i: Optional[str]`
    :   Brokerage (FX Intraday)

    `brkage_f_m: Optional[str]`
    :   Brokerage (FX Margin)

    `brkcollamt: Optional[float]`
    :   Prevalued Collateral Amount

    `brokerage: Optional[str]`
    :   Brokerage amount

    `cash: Optional[float]`
    :   Cash Margin available

    `cbu: Optional[str]`
    :   CAC Buy used

    `collateral: Optional[str]`
    :   Collateral calculated based on uploaded holdings

    `csc: Optional[str]`
    :   CAC Sell Credits

    `daycash: Optional[float]`
    :   Additional leverage amount / Amount added to handle system errors - by broker.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange

    `expo: Optional[str]`
    :   Exposure margin

    `expo_c_i: Optional[str]`
    :   Exposure Margin (Commodity Intraday)

    `expo_c_m: Optional[str]`
    :   Exposure Margin (Commodity Margin)

    `expo_d_i: Optional[str]`
    :   Exposure Margin (Derivative Intraday)

    `expo_d_m: Optional[str]`
    :   Exposure Margin (Derivative Margin)

    `expo_f_i: Optional[str]`
    :   Exposure Margin (FX Intraday)

    `expo_f_m: Optional[str]`
    :   Exposure Margin (FX Margin)

    `grcoll: Optional[str]`
    :   Valuation of uploaded holding pre haircut

    `greexpo_d: Optional[str]`
    :   Gross Exposure derivative

    `grexpo: Optional[str]`
    :   Gross Exposure

    `marginused: Optional[float]`
    :   Total margin / fund used today

    `marprt: Optional[str]`
    :   Covered Product margins

    `marprt_c_b: Optional[str]`
    :   Covered Product margins (Commodity Bracket Order)

    `marprt_c_h: Optional[str]`
    :   Covered Product margins (Commodity High leverage)

    `marprt_d_b: Optional[str]`
    :   Covered Product margins (Derivative Bracket Order)

    `marprt_d_h: Optional[str]`
    :   Covered Product margins (Derivative High leverage)

    `marprt_e_b: Optional[str]`
    :   Covered Product margins (Equity Bracket Order)

    `marprt_e_h: Optional[str]`
    :   Covered Product margins (Equity High leverage)

    `marprt_f_b: Optional[str]`
    :   Covered Product margins (FX Bracket Order)

    `marprt_f_h: Optional[str]`
    :   Covered Product margins (FX High leverage)

    `mtomcurper: Optional[str]`
    :   Mtom current percentage

    `payin: Optional[float]`
    :   Total Amount transferred using Payins today

    `payout: Optional[float]`
    :   Total amount requested for withdrawal today

    `pendordval: Optional[str]`
    :   Pending Order value

    `pendordvallmt: Optional[str]`
    :   Pending order value limit

    `prd: Optional[str]`
    :   Product name

    `premium: Optional[str]`
    :   Premium used

    `premium_c_i: Optional[str]`
    :   Option premium (Commodity Intraday)

    `premium_c_m: Optional[str]`
    :   Option premium (Commodity Margin)

    `premium_d_i: Optional[str]`
    :   Option premium (Derivative Intraday)

    `premium_d_m: Optional[str]`
    :   Option premium (Derivative Margin)

    `premium_f_i: Optional[str]`
    :   Option premium (FX Intraday)

    `premium_f_m: Optional[str]`
    :   Option premium (FX Margin)

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `rpnl: Optional[str]`
    :   Current realized PNL

    `rzpnl_c_i: Optional[str]`
    :   Current realized PNL (Commodity Intraday)

    `rzpnl_c_m: Optional[str]`
    :   Current realized PNL (Commodity Margin)

    `rzpnl_d_i: Optional[str]`
    :   Current realized PNL (Derivative Intraday)

    `rzpnl_d_m: Optional[str]`
    :   Current realized PNL (Derivative Margin)

    `rzpnl_e_c: Optional[str]`
    :   Current realized PNL (Equity Cash n Carry)

    `rzpnl_e_i: Optional[str]`
    :   Current realized PNL (Equity Intraday)

    `rzpnl_e_m: Optional[str]`
    :   Current realized PNL (Equity Margin)

    `rzpnl_f_i: Optional[str]`
    :   Current realized PNL (FX Intraday)

    `rzpnl_f_m: Optional[str]`
    :   Current realized PNL (FX Margin)

    `scripbskmar: Optional[str]`
    :   Scrip basket margin

    `scripbskmar_e_c: Optional[str]`
    :   Scrip basket margin (Equity Cash n Carry)

    `scripbskmar_e_i: Optional[str]`
    :   Scrip basket margin (Equity Intraday)

    `scripbskmar_e_m: Optional[str]`
    :   Scrip basket margin (Equity Margin)

    `seg: Optional[str]`
    :   CM / FO / FX - Segment

    `span: Optional[str]`
    :   Span used

    `span_c_i: Optional[str]`
    :   Span Margin (Commodity Intraday)

    `span_c_m: Optional[str]`
    :   Span Margin (Commodity Margin)

    `span_d_i: Optional[str]`
    :   Span Margin (Derivative Intraday)

    `span_d_m: Optional[str]`
    :   Span Margin (Derivative Margin)

    `span_f_i: Optional[str]`
    :   Span Margin (FX Intraday)

    `span_f_m: Optional[str]`
    :   Span Margin (FX Margin)

    `stat: py_client.common.enums.ResponseStatus`
    :   The limits success or failure status

    `turnover: Optional[str]`
    :   Turnover

    `turnoverlmt: Optional[str]`
    :   Turnover Limit

    `unclearedcash: Optional[float]`
    :   Uncleared Cash (Payin through cheques)

    `unmtom: Optional[str]`
    :   Current unrealized mtom

    `uzpnl_c_i: Optional[str]`
    :   Current unrealized MTOM (Commodity Intraday)

    `uzpnl_c_m: Optional[str]`
    :   Current unrealized MTOM (Commodity Margin)

    `uzpnl_d_i: Optional[str]`
    :   Current unrealized MTOM (Derivative Intraday)

    `uzpnl_d_m: Optional[str]`
    :   Current unrealized MTOM (Derivative Margin)

    `uzpnl_e_c: Optional[str]`
    :   Current unrealized MTOM (Equity Cash n Carry)

    `uzpnl_e_i: Optional[str]`
    :   Current unrealized MTOM (Equity Intraday)

    `uzpnl_e_m: Optional[str]`
    :   Current unrealized MTOM (Equity Margin)

    `uzpnl_f_i: Optional[str]`
    :   Current unrealized MTOM (FX Intraday)

    `uzpnl_f_m: Optional[str]`
    :   Current unrealized MTOM (FX Margin)

    `varelm: Optional[str]`
    :   Var Elm Margin

    `varelm_e_c: Optional[str]`
    :   Var Elm (Equity Cash n Carry)

    `varelm_e_i: Optional[str]`
    :   Var Elm (Equity Intraday)

    `varelm_e_m: Optional[str]`
    :   Var Elm (Equity Margin)