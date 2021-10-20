
"""
Request and response models for get content basket request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetContentBasketRequestModel', 'GetContentBasketResponseModel']

class Basket(BaseModel):
  """
  Singel basket item
  """
  basket: str
  """The basket"""

class GetContentBasketRequestModel(BaseModel):
  """
  The request model for get content basket endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: str
  """Exchange Name"""

class GetContentBasketResponseModel(BaseModel):
  """
  The response model for get content basket endpoint
  """
  stat: ResponseStatus
  """The get content basket success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  basketlist: Optional[List[Basket]]
  """List of baskets"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
