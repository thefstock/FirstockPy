"""
The data source for all watchlist specific requests
"""

from ...utils.datasources import NorenRestDataSource
from . import endpoints

from .models import *

class WatchListDataSource(NorenRestDataSource):
  """
  The datasource for all watch list specific requests
  """
  def get_names(self, model: GetWatchListNamesRequestModel, key: str = None) -> GetWatchListNamesResponseModel:
    """
    Fetch watchlist names

    Args:
      model (GetWatchListNamesRequestModel): The data to be send as GetWatchListNamesRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetWatchListNamesResponseModel: The response as GetWatchListNamesResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_NAMES, key)
    # convert the request to response model
    return GetWatchListNamesResponseModel.parse_raw(response_json)

  def get_watchlist(self, model: GetWatchListRequestModel, key: str = None) -> GetWatchListResponseModel:
    """
    Get scrip list for a given watchlist name

    Args:
      model (GetWatchListRequestModel): The data to be send as GetWatchListRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetWatchListResponseModel: The response as GetWatchListResponseModel.
    """
    
    response_json = self._run_request(model, endpoints.GET_WATCHLIST, key)
    # convert the request to response model
    return GetWatchListResponseModel.parse_raw(response_json)

  def search_scrips(self, model: SearchScripsRequestModel, key: str = None) -> SearchScripsResponseModel:
    """
    Search for scrips

    Args:
      model (SearchScripsRequestModel): The data to be send as SearchScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SearchScripsResponseModel: The response as SearchScripsResponseModel.
    """
    response_json = self._run_request(model, endpoints.SEARCH_SCRIPS, key)
    # convert the request to response model
    return SearchScripsResponseModel.parse_raw(response_json)

  def add_scrips(self, model: AddScripsRequestModel, key: str = None) -> AddScripsResponseModel:
    """
    Add multiple scrips to a watchlist

    Args:
      model (AddScripsRequestModel): The data to be send as AddScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      AddScripsResponseModel: The response as AddScripsResponseModel.
    """
    response_json = self._run_request(model, endpoints.ADD_SCRIPS, key)
    # convert the request to response model
    return AddScripsResponseModel.parse_raw(response_json)

  def delete_scrips(self, model: DeleteScripsRequestModel, key: str = None) -> DeleteScripsResponseModel:
    """
    Delete scrips from a watchlist

    Args:
      model (DeleteScripsRequestModel): The data to be send as DeleteScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      DeleteScripsResponseModel: The response as DeleteScripsResponseModel.
    """
    response_json = self._run_request(model, endpoints.DELETE_SCRIPS, key)
    # convert the request to response model
    return DeleteScripsResponseModel.parse_raw(response_json)

  def get_security_info(self, model: GetSecurityInfoRequestModel, key: str = None) -> GetSecurityInfoResponseModel:
    """
    Get security info

    Args:
      model (GetSecurityInfoRequestModel): The data to be send as GetSecurityInfoRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetSecurityInfoResponseModel: The response as GetSecurityInfoResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_SECURITY_INFO, key)
    # convert the request to response model
    return GetSecurityInfoResponseModel.parse_raw(response_json)

  def get_quotes(self, model: GetQuotesRequestModel, key: str = None) -> GetQuotesResponseModel:
    """
    Get quotes

    Args:
      model (GetQuotesRequestModel): The data to be send as GetQuotesRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetQuotesResponseModel: The response as GetQuotesResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_QUOTES, key)
    # convert the request to response model
    return GetQuotesResponseModel.parse_raw(response_json)

  def get_predefined_watchlists(self, model: GetPredefinedWatchListsRequestModel, key: str = None) -> GetPredefinedWatchListsResponseModel:
    """
    Get list of predefined MWs

    Args:
      model (GetPredefinedWatchListsRequestModel): The data to be send as GetPredefinedWatchListsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetPredefinedWatchListsResponseModel: The response as GetPredefinedWatchListsResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_PREDEFINED_WATCHLISTS, key)
    # convert the request to response model
    return GetPredefinedWatchListsResponseModel.parse_raw(response_json)

  def get_predefined_scrips(self, model: GetPredefinedScripsRequestModel, key: str = None) -> GetPredefinedScripsResponseModel:
    """
    Get list of predefined MW scrips

    Args:
      model (GetPredefinedScripsRequestModel): The data to be send as GetPredefinedScripsRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetPredefinedScripsResponseModel: The response as GetPredefinedScripsResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_PREDEFINED_SCRIPS, key)
    # convert the request to response model
    return GetPredefinedScripsResponseModel.parse_raw(response_json)