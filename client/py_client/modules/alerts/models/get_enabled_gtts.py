
"""
Request and response models for get enabled gtts request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import AlertType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetEnabledGttsRequestModel', 'GetEnabledGttsResponseModel']

class GetEnabledGttsRequestModel(BaseModel):
  """
  The request model for get enabled gtts endpoint
  """
  uid: str
  """The user id of the login user"""

class GetEnabledGttsResponseModel(BaseModel):
  """
  The response model for get enabled gtts endpoint
  """
  stat: ResponseStatus
  """The get enabled gtts success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  ai_ts: Optional[List[AlertType]]
  """List of alert types"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
