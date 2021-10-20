"""
The request and response models for search scrip request
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....common.models import Scrip
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['SearchScripsRequestModel', 'SearchScripsResponseModel']

class SearchScripsRequestModel(BaseModel):
  """
  The request model for search scrip endpoint
  """
  uid: str
  """The user id of the login user"""
  stext: str
  """Search Text"""
  exch: Optional[str]
  """Exchange (Select from ‘exarr’ Array provided in User Details response)"""

class SearchScripsResponseModel(BaseModel):
  """
  The response model for search scrip endpoint
  """
  stat: ResponseStatus
  """The search scrips success or failure status"""
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