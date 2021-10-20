
"""
Request and response models for time price series request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder
from ....utils.encoders import build_dumber, timestamp_encoder

__all__ = ['TimePriceSeriesRequestModel', 'TimePriceSeriesResponseModel']

class TimePriceSeriesRequestModel(BaseModel):
  """
  The request model for time price series endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: str 
  """Exchange"""
  token: str
  """Token"""
  st: datetime
  """Start time"""
  et: datetime
  """End Time"""

  class Config:
    """model configuration"""
    json_dumps = build_dumber({
      "st": timestamp_encoder(),
      "et": timestamp_encoder()
    })

class TimePriceSeriesResponseModel(BaseModel):
  """
  The response model for time price series endpoint
  """
  stat: ResponseStatus
  """The time price series success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  time: Optional[datetime]
  """DD/MM/CCYY hh:mm:ss"""
  into: Optional[str]
  """Interval open"""
  inth: Optional[str]
  """Interval high"""
  intl: Optional[str]
  """Interval low"""
  intc: Optional[str]
  """Interval close"""
  intvwap: Optional[str]
  """Interval vwap"""
  intv: Optional[str]
  """Interval volume"""
  v: Optional[str]
  """volume"""
  intoi: Optional[str]
  """Interval io change"""
  oi: Optional[str]
  """oi """
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder(),
      "time": datetime_decoder()
    })
