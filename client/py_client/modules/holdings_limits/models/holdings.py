
"""
Request and response models for holdings request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import ExchTsym
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['HoldingsRequestModel', 'HoldingsResponseModel']

class HoldingsRequestModel(BaseModel):
  """
  The request model for holdings endpoint
  """
  uid: str
  """The user id of the login user"""
  actid: str
  """Account id of the logged in user."""
  prd: str
  """Product name"""

class HoldingsResponseModel(BaseModel):
  """
  The response model for holdings endpoint
  """
  stat: ResponseStatus
  """The holdings success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  exch_tsym: Optional[List[ExchTsym]]
  """Array of objects exch_tsym objects as defined below."""
  holdqty: Optional[float]
  """Holding quantity"""
  dpqty: Optional[float]
  """DP Holding quantity"""
  npoadqty: Optional[float]
  """Non Poa display quantity"""
  colqty: Optional[float]
  """Collateral quantity"""
  benqty: Optional[float]
  """Beneficiary quantity"""
  unplgdqty: Optional[float]
  """Unpledged quantity"""
  brkcolqty: Optional[float]
  """Broker Collateral"""
  btstqty: Optional[float]
  """BTST quantity"""
  btstcolqty: Optional[float]
  """BTST Collateral quantity"""
  usedqty: Optional[float]
  """Holding used today"""
  upldprc: Optional[float]
  """Average price uploaded along with holdings """
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
