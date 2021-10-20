
"""
Request and response models for get broker message request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetBrokerMessageRequestModel', 'GetBrokerMessageResponseModel']

class GetBrokerMessageRequestModel(BaseModel):
  """
  The request model for get broker message endpoint
  """
  uid: str
  """The user id of the login user"""

class GetBrokerMessageResponseModel(BaseModel):
  """
  The response model for get broker message endpoint
  """
  stat: ResponseStatus
  """The get broker message success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  dmsg: Optional[str]
  """This will be present only in case of success"""
  norentm: Optional[datetime]
  """Noren Time"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder(),
      "norentm": datetime_decoder()
    })
