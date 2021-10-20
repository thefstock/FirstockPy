
"""
Request and response models for get enabled alert types request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import AlertType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetEnabledAlertTypesRequestModel', 'GetEnabledAlertTypesResponseModel']

class GetEnabledAlertTypesRequestModel(BaseModel):
  """
  The request model for get enabled alert types endpoint
  """
  uid: str
  """The user id of the login user"""

class GetEnabledAlertTypesResponseModel(BaseModel):
  """
  The response model for get enabled alert types endpoint
  """
  stat: ResponseStatus
  """The get enabled alert types success or failure status"""
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
