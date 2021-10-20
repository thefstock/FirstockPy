"""
Common models used across the project
"""

from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from .enums import PriceType, TransactionType
from ..utils.decoders import build_loader, datetime_decoder

class Product(BaseModel):
  """
  The product model
  """
  prd: str
  """The product name"""
  s_prdt_ali: str
  """The product display name"""
  exch: List[str]
  """List of strings with enabled, allowed exchange names"""

class BankDetails(BaseModel):
  """
  The bank details model
  """
  bankn: Optional[str]
  """Bank Name"""
  acctnum: Optional[str]
  """Account Number"""

class DpAccountNumber(BaseModel):
  """
  The dp account number model
  """
  dpnum: Optional[str]

class Scrip(BaseModel):
  """
  The scrip model
  """
  exch: Optional[str]
  """Exchange"""
  tsym: Optional[str]
  """Trading symbol of the scrip (contract)"""
  token: Optional[str]
  """Token of the scrip (contract)"""
  pp: Optional[float]
  """Price precision"""
  ti: Optional[float]
  """Tick size"""
  ls: Optional[float]
  """Lot size"""

class BasketList(BaseModel):
  """
  The basketlist model
  """
  exch: str
  """Exchange (Select from ‘exarr’ Array provided in User Details response)"""
  tsym: str
  """Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)"""
  qty: str
  """Order Quantity"""
  prc: str
  """Order Price"""
  trgprc: Optional[str]
  """Only to be sent in case of SL / SL-M order."""
  prd: str
  """C / M / H Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call)"""
  trantype: TransactionType
  """BUY or SELL"""
  prctyp: PriceType
  """LMT / MKT / SL-LMT/ SL-MKT"""

class IndexTokenPair(BaseModel):
  """
  The basket criteria pair
  """
  idxname: str
  """The index name"""
  token: str
  """Index token used to subscribe"""

class BasketCriteriaPair(BaseModel):
  """
  The basket criteria pair
  """
  bskt: str
  """The basket name"""
  crt: str
  """The criteria"""

class TBContract(BaseModel):
  """
  Top/Bottom contract
  """
  tsym: Optional[str] 
  """Trading symbol"""
  lp: Optional[str] 
  """LTP"""
  c: Optional[str] 
  """Previous Close price"""
  v: Optional[str] 
  """volume"""
  value: Optional[str] 
  """Total traded value"""
  oi: Optional[str] 
  """Open interest"""
  pc: Optional[str] 
  """LTP percentage change"""

class AlertType(BaseModel):
  """
  The alert type model
  """
  ai_t: str
  """Alert type"""

class TradeDate(BaseModel):
  """
  The trade date model
  """
  trd_date: date

  class Config:
    """The model config"""
    json_dumps = {
      "trd_date": datetime_decoder(transform=lambda dt: dt.date())
    }

class ExchTsym(BaseModel):
  """The exch_tsym model"""
  exch: Optional[str]
  """NSE, BSE, NFO ... Exchange"""
  tsym: Optional[str]
  """Trading symbol of the scrip (contract)"""
  token: Optional[str]
  """Token of the scrip (contract)"""
  pp: Optional[str]
  """Price precision"""
  ti: Optional[float]
  """Tick size"""
  ls: Optional[float]
  """Lot size"""