
"""
Request and response models for get content list request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetContentListRequestModel', 'GetContentListResponseModel']

class GetContentListRequestModel(BaseModel):
  """
  The request model for get content list endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: str
  """Exchange Name"""
  condition_name: str
  """condition list"""
  basket: Optional[str]
  """Basket Name"""

class GetContentListResponseModel(BaseModel):
  """
  The response model for get content list endpoint
  """
  stat: ResponseStatus
  """The get content list success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  tsym: Optional[str]
  """Trading symbol"""
  lp: Optional[float]
  """LTP"""
  c: Optional[float]
  """Close price"""
  h: Optional[float]
  """High price"""
  l: Optional[float]
  """Low price"""
  ap: Optional[float]
  """Average trade price"""
  v: Optional[float]
  """Volume"""
  ltt: Optional[str]
  """Last trade time"""
  pc: Optional[float]
  """Percentage change """
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
