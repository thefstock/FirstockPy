"""
Request and Response model for exit sno order request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['ExitSnoOrderRequestModel', 'ExitSnoOrderResponseModel']

class ExitSnoOrderRequestModel(BaseModel):
  """
  The request model for exit sno order  request
  """
  uid: str
  """Logged in User Id"""
  norenordno: str
  """Noren order number, which needs to be cancelled"""
  prd: str
  """Allowed for only H and B products (Cover order and bracket order)"""

class ExitSnoOrderResponseModel(BaseModel):
  """
  The response model for exit sno order endpoint
  """
  stat: ResponseStatus
  """The exit sno success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  dmsg: Optional[str]
  """Display message, (will be present only in case of success)."""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })