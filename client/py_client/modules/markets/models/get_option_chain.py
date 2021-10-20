
"""
Request and response models for get option chain request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetOptionChainRequestModel', 'GetOptionChainResponseModel', 'MarketOptionChain']

class MarketOptionChain(BaseModel):
  """
  Market option chain
  """
  exch: Optional[str]
  """Exchange"""
  tsym: Optional[str]
  """Trading symbol of the scrip (contract)"""
  token: Optional[str]
  """Token of the scrip (contract)"""
  optt: Optional[str]
  """Option Type"""
  strprc: Optional[str]
  """Strike price"""
  pp: Optional[str]
  """Price precision"""
  ti: Optional[str]
  """Tick size"""
  ls: Optional[str]
  """Lot size"""

class GetOptionChainRequestModel(BaseModel):
  """
  The request model for get option chain endpoint
  """
  uid: str
  """The user id of the login user"""
  tsym: str 
  """
  Trading symbol of any of the option or future. Option chain for that underlying will be returned.
  (use url encoding to avoid special char error for symbols like M&M)
  """
  exch: str 
  """Exchange"""
  strprc: str 
  """Mid price for option chain selection"""
  cnt: str
  """
  Number of strike to return on one side of the mid price for PUT and CALL. 
  (example cnt is 4, total 16 contracts will be returned, if cnt is is 5 total 20 contract will be returned)
  """

class GetOptionChainResponseModel(BaseModel):
  """
  The response model for get option chain endpoint
  """
  stat: ResponseStatus
  """The get option chain success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  values: Optional[List[MarketOptionChain]]
  """List of items"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
