
"""
Datasource for handling funds operations
"""
from ...utils.datasources import NorenRestDataSource
from . import endpoints
from .models import *

class FundsDataSource(NorenRestDataSource):
  """
  Datasource for handling funds operations
  """
  def get_max_payout_amount(self, model: GetMaxPayoutAmountRequestModel, key: str = None) -> GetMaxPayoutAmountResponseModel:
    """
    Get max payout amount

    Args:
      model (GetMaxPayoutAmountRequestModel): The data to be send as GetMaxPayoutAmountRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetMaxPayoutAmountResponseModel: The response as GetMaxPayoutAmountResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_MAX_PAYOUT_AMOUNT, key)
    # convert the request to response model
    return GetMaxPayoutAmountResponseModel.parse_raw(response_json)

  def get_content_basket(self, model: GetContentBasketRequestModel, key: str = None) -> GetContentBasketResponseModel:
    """
    Get content basket

    Args:
      model (GetContentBasketRequestModel): The data to be send as GetContentBasketRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetContentBasketResponseModel: The response as GetContentBasketResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_CONTENT_BASKET, key)
    # convert the request to response model
    return GetContentBasketResponseModel.parse_raw(response_json)

  def get_content_list(self, model: GetContentListRequestModel, key: str = None) -> GetContentListResponseModel:
    """
    Get content list

    Args:
      model (GetContentListRequestModel): The data to be send as GetContentListRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetContentListResponseModel: The response as GetContentListResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_CONTENT_LIST, key)
    # convert the request to response model
    return GetContentListResponseModel.parse_raw(response_json)
