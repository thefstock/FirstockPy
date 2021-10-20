"""
The request and response models for get watchlist names request
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetWatchListNamesRequestModel', 'GetWatchListNamesResponseModel']

class GetWatchListNamesRequestModel(BaseModel):
  """
  The request model for get watchlist names endpoint
  """
  uid: str
  """The user id of the login user"""

class GetWatchListNamesResponseModel(BaseModel):
  """
  The response model for get watchlist names endpoint
  """
  stat: ResponseStatus
  """The get names success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  values: List[str]
  """Watch List names as a json array of strings."""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })