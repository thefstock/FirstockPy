"""
The request and response models for get quotes request
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetQuotesRequestModel', 'GetQuotesResponseModel']

class GetQuotesRequestModel(BaseModel):
  """
  The request model for get quotes endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: Optional[str]
  """Exchange"""
  token: Optional[str]
  """Contract Token"""

class GetQuotesResponseModel(BaseModel):
  """
  The response model for get quotes endpoint
  """
  stat: ResponseStatus
  """The get scrips success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  emsg: Optional[str]
  """Error message if the request failed"""
  exch: Optional[str]
  """Exchange"""
  tsym: Optional[str]
  """Trading Symbol"""
  cname: Optional[str]
  """Company Name"""
  symnam: Optional[str]
  """Symbol Name"""
  seg: Optional[str]
  """Segment"""
  instname: Optional[str]
  """Intrument Name"""
  isin: Optional[str]
  """ISIN"""
  ti: Optional[float]
  """Tick Size"""
  ls: Optional[float]
  """Lot Size"""
  pp: Optional[float]
  """Price precision"""
  mult: Optional[float]
  """Multiplier"""
  token: Optional[str]
  """Contract Token"""
  prcftr_d: Optional[str]
  """((GN / GD) * (PN/PD))"""
  uc: Optional[float]
  """Upper circuit limit"""
  lc: Optional[float]
  """Lower circuit limit"""
  lp: Optional[float]
  """LTP"""
  h: Optional[float]
  """Day High Price"""
  l: Optional[float]
  """Day Low Price"""
  v: Optional[float]
  """Volume"""
  ltq: Optional[float]
  """Last trade quantity"""
  ltt: Optional[str]
  """Last trade time"""
  bp1: Optional[float]
  """Best Buy Price"""
  sp1: Optional[float]
  """Best Sell Price"""
  bp2: Optional[float]
  """Best Buy Price"""
  sp2: Optional[float]
  """Best Sell Price"""
  bp3: Optional[float]
  """Best Buy Price"""
  sp3: Optional[float]
  """Best Sell Price"""
  bp4: Optional[float]
  """Best Buy Price"""
  sp4: Optional[float]
  """Best Sell Price"""
  bp5: Optional[float]
  """Best Buy Price"""
  sp5: Optional[float]
  """Best Sell Price"""
  bq1: Optional[float]
  """Best Buy Quantity"""
  sq1: Optional[float]
  """Best Sell Quantity"""
  bq2: Optional[float]
  """Best Buy Quantity"""
  sq2: Optional[float]
  """Best Sell Quantity"""
  bq3: Optional[float]
  """Best Buy Quantity"""
  sq3: Optional[float]
  """Best Sell Quantity"""
  bq4: Optional[float]
  """Best Buy Quantity"""
  sq4: Optional[float]
  """Best Sell Quantity"""
  bq5: Optional[float]
  """Best Buy Quantity"""
  sq5: Optional[float]
  """Best Sell Quantity"""
  bo1: Optional[float]
  """Best Buy Orders"""
  so1: Optional[float]
  """Best Sell Orders"""
  bo2: Optional[float]
  """Best Buy Orders"""
  so2: Optional[float]
  """Best Sell Orders"""
  bo3: Optional[float]
  """Best Buy Orders"""
  so3: Optional[float]
  """Best Sell Orders"""
  bo4: Optional[float]
  """Best Buy Orders"""
  so4: Optional[float]
  """Best Sell Orders"""
  bo5: Optional[float]
  """Best Buy Orders"""
  so5: Optional[float]
  """Best Sell Orders"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })