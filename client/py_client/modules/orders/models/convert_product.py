"""
Request and Response model for product conversion request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['ConvertProductRequestModel', 'ConvertProductResponseModel']

class ConvertProductRequestModel(BaseModel):
  """
  The request model for product conversion request
  """
  uid: str
  """Logged in User Id"""
  tsym: str
  """
  Unique id of contract on which order was placed.
  Can’t be modified, must be the same as that of original order.
  (use url encoding to avoid special char error for symbols like M&M)
  """
  qty: float
  """Quantity to be converted."""
  uid: str
  """User id of the logged in user."""
  actid: str
  """Account id"""
  prd: str
  """Product to which the user wants to convert position."""
  prevprd: str
  """Original product of the position."""
  trantype: TransactionType
  """Transaction type"""
  postype: str
  """Day / CF Converting Day or Carry forward position"""
  ordersource: Optional[str]
  """MOB For Logging"""

class ConvertProductResponseModel(BaseModel):
  """
  The response model for product conversion endpoint
  """
  stat: ResponseStatus
  """The product conversion success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })