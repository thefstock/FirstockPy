"""
The request and response models for add scrips to watchlist request
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder
from ....utils.encoders import build_dumber, list_encoder

__all__ = ['AddScripsRequestModel', 'AddScripsResponseModel']

class AddScripsRequestModel(BaseModel):
  """
  The request model for add scrips to watchlist endpoint
  """
  uid: str
  """The user id of the login user"""
  wlname: str
  """Name of the Watchlist, for which scrip list is required"""
  scrips: List[str]
  """List of scrips"""
  class Config:
    """model configuration"""
    json_dumps = build_dumber({
      "scrips": list_encoder('|')
    })

class AddScripsResponseModel(BaseModel):
  """
  The response model for add scrips to watchlist endpoint
  """
  stat: ResponseStatus
  """The add scrips success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })