"""
Request and Response model for cancel order request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['CancelOrderRequestModel', 'CancelOrderResponseModel']

class CancelOrderRequestModel(BaseModel):
  """
  The request model for cancel order  request
  """
  uid: str
  """Logged in User Id"""
  norenordno: str
  """Noren order number, which needs to be cancelled"""

class CancelOrderResponseModel(BaseModel):
  """
  The response model for cancel order endpoint
  """
  stat: ResponseStatus
  """The cancel order success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  result: Optional[str]
  """Noren Order number of the order modified."""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })