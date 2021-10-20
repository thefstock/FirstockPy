"""
The request and response models for get predefined scrips request
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....common.models import Scrip
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetPredefinedScripsRequestModel', 'GetPredefinedScripsResponseModel']

class GetPredefinedScripsRequestModel(BaseModel):
  """
  The request model for get predefined scrips endpoint
  """
  uid: str
  """The user id of the login user"""
  wlname: str
  """Name of the Watchlist, for which scrip list is required"""

class GetPredefinedScripsResponseModel(BaseModel):
  """
  The response model for get predefined scrips endpoint
  """
  stat: ResponseStatus
  """The get predefined scrips success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  values: List[Scrip]
  """Watch List names as a json array of strings."""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })