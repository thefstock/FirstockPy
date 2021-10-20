"""
Request and response models for set device pin
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import RequestSourceType, ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['SetDevicePinRequestModel', 'SetDevicePinResponseModel']

class SetDevicePinRequestModel(BaseModel):
  """
  The data model for set device pin request
  """
  uid: str
  """User Id"""
  imei: str
  """IMEI or device unique fingerprint"""
  source: RequestSourceType
  """Access type"""
  dpin: str
  """New pin"""

class SetDevicePinResponseModel(BaseModel):
  """
  The data model for set device pin response
  """
  stat: ResponseStatus
  """The set device pin success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful setting of new pin."""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })