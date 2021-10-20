
"""
Request and response models for limits request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['LimitsRequestModel', 'LimitsResponseModel']

class LimitsRequestModel(BaseModel):
  """
  The request model for limits endpoint
  """
  uid: str
  """The user id of the login user"""
  actid: str
  """Account id of the logged in user."""
  prd: Optional[str]
  """Product name"""
  exch: Optional[str]
  """Exchange"""
  seg: Optional[str]
  """CM / FO / FX - Segment"""

class LimitsResponseModel(BaseModel):
  """
  The response model for limits endpoint
  """
  stat: ResponseStatus
  """The limits success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  actid: Optional[str]
  """Account id of the logged in user."""
  prd: Optional[str]
  """Product name"""
  exch: Optional[str]
  """Exchange"""
  seg: Optional[str]
  """CM / FO / FX - Segment"""
  cash: Optional[float]
  """Cash Margin available"""
  payin: Optional[float]
  """Total Amount transferred using Payins today"""
  payout: Optional[float]
  """Total amount requested for withdrawal today"""
  brkcollamt: Optional[float]
  """Prevalued Collateral Amount"""
  unclearedcash: Optional[float]
  """Uncleared Cash (Payin through cheques)"""
  daycash: Optional[float]
  """Additional leverage amount / Amount added to handle system errors - by broker."""
  marginused: Optional[float]
  """Total margin / fund used today"""
  mtomcurper: Optional[str]
  """Mtom current percentage"""

  cbu: Optional[str]
  """CAC Buy used"""
  csc: Optional[str]
  """CAC Sell Credits"""
  rpnl: Optional[str]
  """Current realized PNL"""
  unmtom: Optional[str]
  """Current unrealized mtom"""
  marprt: Optional[str]
  """Covered Product margins"""
  span: Optional[str]
  """Span used"""
  expo: Optional[str]
  """Exposure margin"""
  premium: Optional[str]
  """Premium used"""
  varelm: Optional[str]
  """Var Elm Margin"""
  grexpo: Optional[str]
  """Gross Exposure"""
  greexpo_d: Optional[str]
  """Gross Exposure derivative"""
  scripbskmar: Optional[str]
  """Scrip basket margin"""
  addscripbskmrg: Optional[str]
  """Additional scrip basket margin"""
  brokerage: Optional[str]
  """Brokerage amount"""
  collateral: Optional[str]
  """Collateral calculated based on uploaded holdings"""
  grcoll: Optional[str]
  """Valuation of uploaded holding pre haircut"""
  turnoverlmt: Optional[str]
  """Turnover Limit"""
  pendordvallmt: Optional[str]
  """Pending order value limit"""
  turnover: Optional[str]
  """Turnover"""
  pendordval: Optional[str]
  """Pending Order value """
  rzpnl_e_i: Optional[str]
  """Current realized PNL (Equity Intraday)"""
  rzpnl_e_m: Optional[str]
  """Current realized PNL (Equity Margin)"""
  rzpnl_e_c: Optional[str]
  """Current realized PNL (Equity Cash n Carry)"""
  rzpnl_d_i: Optional[str]
  """Current realized PNL (Derivative Intraday)"""
  rzpnl_d_m: Optional[str]
  """Current realized PNL (Derivative Margin)"""
  rzpnl_f_i: Optional[str]
  """Current realized PNL (FX Intraday)"""
  rzpnl_f_m: Optional[str]
  """Current realized PNL (FX Margin)"""
  rzpnl_c_i: Optional[str]
  """Current realized PNL (Commodity Intraday)"""
  rzpnl_c_m: Optional[str]
  """Current realized PNL (Commodity Margin)"""
  uzpnl_e_i: Optional[str]
  """Current unrealized MTOM (Equity Intraday)"""
  uzpnl_e_m: Optional[str]
  """Current unrealized MTOM (Equity Margin)"""
  uzpnl_e_c: Optional[str]
  """Current unrealized MTOM (Equity Cash n Carry)"""
  uzpnl_d_i: Optional[str]
  """Current unrealized MTOM (Derivative Intraday)"""
  uzpnl_d_m: Optional[str]
  """Current unrealized MTOM (Derivative Margin)"""
  uzpnl_f_i: Optional[str]
  """Current unrealized MTOM (FX Intraday)"""
  uzpnl_f_m: Optional[str]
  """Current unrealized MTOM (FX Margin)"""
  uzpnl_c_i: Optional[str]
  """Current unrealized MTOM (Commodity Intraday)"""
  uzpnl_c_m: Optional[str]
  """Current unrealized MTOM (Commodity Margin)"""
  span_d_i: Optional[str]
  """Span Margin (Derivative Intraday)"""
  span_d_m: Optional[str]
  """Span Margin (Derivative Margin)"""
  span_f_i: Optional[str]
  """Span Margin (FX Intraday)"""
  span_f_m: Optional[str]
  """Span Margin (FX Margin)"""
  span_c_i: Optional[str]
  """Span Margin (Commodity Intraday)"""
  span_c_m: Optional[str]
  """Span Margin (Commodity Margin)"""
  expo_d_i: Optional[str]
  """Exposure Margin (Derivative Intraday)"""
  expo_d_m: Optional[str]
  """Exposure Margin (Derivative Margin)"""
  expo_f_i: Optional[str]
  """Exposure Margin (FX Intraday)"""
  expo_f_m: Optional[str]
  """Exposure Margin (FX Margin)"""
  expo_c_i: Optional[str]
  """Exposure Margin (Commodity Intraday)"""
  expo_c_m: Optional[str]
  """Exposure Margin (Commodity Margin)"""
  premium_d_i: Optional[str]
  """Option premium (Derivative Intraday)"""
  premium_d_m: Optional[str]
  """Option premium (Derivative Margin)"""
  premium_f_i: Optional[str]
  """Option premium (FX Intraday)"""
  premium_f_m: Optional[str]
  """Option premium (FX Margin)"""
  premium_c_i: Optional[str]
  """Option premium (Commodity Intraday)"""
  premium_c_m: Optional[str]
  """Option premium (Commodity Margin)"""
  varelm_e_i: Optional[str]
  """Var Elm (Equity Intraday)"""
  varelm_e_m: Optional[str]
  """Var Elm (Equity Margin)"""
  varelm_e_c: Optional[str]
  """Var Elm (Equity Cash n Carry)"""
  marprt_e_h: Optional[str]
  """Covered Product margins (Equity High leverage)"""
  marprt_e_b: Optional[str]
  """Covered Product margins (Equity Bracket Order)"""
  marprt_d_h: Optional[str]
  """Covered Product margins (Derivative High leverage)"""
  marprt_d_b: Optional[str]
  """Covered Product margins (Derivative Bracket Order)"""
  marprt_f_h: Optional[str]
  """Covered Product margins (FX High leverage)"""
  marprt_f_b: Optional[str]
  """Covered Product margins (FX Bracket Order)"""
  marprt_c_h: Optional[str]
  """Covered Product margins (Commodity High leverage)"""
  marprt_c_b: Optional[str]
  """Covered Product margins (Commodity Bracket Order)"""
  scripbskmar_e_i: Optional[str]
  """Scrip basket margin (Equity Intraday)"""
  scripbskmar_e_m: Optional[str]
  """Scrip basket margin (Equity Margin)"""
  scripbskmar_e_c: Optional[str]
  """Scrip basket margin (Equity Cash n Carry)"""
  addscripbskmrg_d_i: Optional[str]
  """Additional scrip basket margin (Derivative Intraday)"""
  addscripbskmrg_d_m: Optional[str]
  """Additional scrip basket margin (Derivative Margin)"""
  addscripbskmrg_f_i: Optional[str]
  """Additional scrip basket margin (FX Intraday)"""
  addscripbskmrg_f_m: Optional[str]
  """Additional scrip basket margin (FX Margin)"""
  addscripbskmrg_c_i: Optional[str]
  """Additional scrip basket margin (Commodity Intraday)"""
  addscripbskmrg_c_m: Optional[str]
  """Additional scrip basket margin (Commodity Margin)"""
  brkage_e_i: Optional[str]
  """Brokerage (Equity Intraday)"""
  brkage_e_m: Optional[str]
  """Brokerage (Equity Margin)"""
  brkage_e_c: Optional[str]
  """Brokerage (Equity CAC)"""
  brkage_e_h: Optional[str]
  """Brokerage (Equity High Leverage)"""
  brkage_e_b: Optional[str]
  """Brokerage (Equity Bracket Order)"""
  brkage_d_i: Optional[str]
  """Brokerage (Derivative Intraday)"""
  brkage_d_m: Optional[str]
  """Brokerage (Derivative Margin)"""
  brkage_d_h: Optional[str]
  """Brokerage (Derivative High Leverage)"""
  brkage_d_b: Optional[str]
  """Brokerage (Derivative Bracket Order)"""
  brkage_f_i: Optional[str]
  """Brokerage (FX Intraday)"""
  brkage_f_m: Optional[str]
  """Brokerage (FX Margin)"""
  brkage_f_h: Optional[str]
  """Brokerage (FX High Leverage)"""
  brkage_f_b: Optional[str]
  """Brokerage (FX Bracket Order)"""
  brkage_c_i: Optional[str]
  """Brokerage (Commodity Intraday)"""
  brkage_c_m: Optional[str]
  """Brokerage (Commodity Margin)"""
  brkage_c_h: Optional[str]
  """Brokerage (Commodity High Leverage)"""
  brkage_c_b: Optional[str]
  """Brokerage (Commodity Bracket Order)"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
