
"""
Request and response models for get pending alert request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus, AlertValidity
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetPendingAlertRequestModel', 'GetPendingAlertResponseModel']

class GetPendingAlertRequestModel(BaseModel):
  """
  The request model for get pending alert endpoint
  """
  uid: str
  """The user id of the login user"""

class GetPendingAlertResponseModel(BaseModel):
  """
  The response model for get pending alert endpoint
  """
  stat: ResponseStatus
  """The get pending alert success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  al_id: Optional[str]
  """The id of the alert to modify"""
  tsym: Optional[str]
  """Trading symbol"""
  exch: Optional[str]
  """Exchange Segment"""
  ai_t: Optional[str]
  """Alert Type"""
  token: Optional[str]
  """Contract token"""
  validity: AlertValidity
  """DAY or GTT Validity"""
  remarks: Optional[str]
  """Any message Entered during order entry."""
  d: Optional[str]
  """Data to be compared with LTP"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
