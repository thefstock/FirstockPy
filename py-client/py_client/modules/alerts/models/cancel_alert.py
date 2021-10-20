
"""
Request and response models for cancel alert request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['CancelAlertRequestModel', 'CancelAlertResponseModel']

class CancelAlertRequestModel(BaseModel):
  """
  The request model for cancel alert endpoint
  """
  uid: str
  """The user id of the login user"""
  al_id: str
  """Alert Id"""

class CancelAlertResponseModel(BaseModel):
  """
  The response model for cancel alert endpoint
  """
  stat: ResponseStatus
  """The cancel alert success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  al_id: Optional[str]
  """Alert Id"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
