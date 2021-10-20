"""
The request and response models for get security info request
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetSecurityInfoRequestModel', 'GetSecurityInfoResponseModel']

class GetSecurityInfoRequestModel(BaseModel):
  """
  The request model for get security infoendpoint
  """
  uid: str
  """The user id of the login user"""
  exch: Optional[str]
  """Exchange"""
  token: Optional[str]
  """Contract Token"""

class GetSecurityInfoResponseModel(BaseModel):
  """
  The response model for get security info endpoint
  """
  stat: ResponseStatus
  """The get security info success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  emsg: Optional[str]
  """Error message if the request failed"""
  exch: Optional[str]
  """Exchange"""
  tsym: Optional[str]
  """Trading Symbol"""
  cname: Optional[str]
  """Company Name"""
  symnam: Optional[str]
  """Symbol Name"""
  seg: Optional[str]
  """Segment"""
  exd: Optional[str]
  """Expiry Date"""
  instname: Optional[str]
  """Intrument Name"""
  strprc: Optional[str]
  """Strike Price"""
  optt: Optional[str]
  """Option Type"""
  isin: Optional[str]
  """ISIN"""
  ti: Optional[float]
  """Tick Size"""
  ls: Optional[float]
  """Lot Size"""
  pp: Optional[float]
  """Price precision"""
  mult: Optional[float]
  """Multiplier"""
  gp_nd: Optional[str]
  """gn/gd * pn/pd"""
  prcunt: Optional[float]
  """Price Units"""
  prcqqty: Optional[float]
  """Price Quote Qty"""
  trdunt: Optional[str]
  """Trade Units"""
  delunt: Optional[str]
  """Delivery Units"""
  frzqty: Optional[float]
  """Freeze Qty"""
  gsmind: Optional[str]
  """scripupdate Gsm Ind"""
  elmbmrg: Optional[str]
  """Elm Buy Margin"""
  elmsmrg: Optional[str]
  """Elm Sell Margin"""
  addbmrg: Optional[str]
  """Additional Long Margin"""
  addsmrg: Optional[str]
  """Additional Short Margin"""
  splbmrg: Optional[str]
  """Special Long Margin"""
  splsmrg: Optional[str]
  """Special Short Margin"""
  delmrg: Optional[str]
  """Delivery Margin"""
  tenmrg: Optional[str]
  """Tender Margin"""
  tenstrd: Optional[str]
  """Tender Start Date"""
  tenendd: Optional[str]
  """Tender End Eate"""
  exestrd: Optional[str]
  """Exercise Start Date"""
  exeendd: Optional[str]
  """Exercise End Date"""
  elmmrg: Optional[str]
  """Elm Margin"""
  varmrg: Optional[str]
  """Var Margin"""
  expmrg: Optional[str]
  """Exposure Margin"""
  token: Optional[str]
  """Contract Token"""
  prcftr_d: Optional[str]
  """((GN / GD) * (PN/PD))"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })