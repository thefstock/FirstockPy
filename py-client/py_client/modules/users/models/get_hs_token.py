"""
Request and response models for get HS token request
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetHsTokenRequestModel', 'GetHsTokenResponseModel']

class GetHsTokenRequestModel(BaseModel):
  """
  The request model for get HS token endpoint
  """
  uid: str

class GetHsTokenResponseModel(BaseModel):
  """
  The response model for get HS token endpoint
  """
  stat: ResponseStatus
  """The logout success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  hstk: Optional[str]
  """One time Token to be sent to BackOffice or third party link"""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
