
"""
Datasource for handling alerts operations
"""
from ...utils.datasources import NorenRestDataSource
from . import endpoints

from .models import *


class AlertsDataSource(NorenRestDataSource):
  """
  Datasource for handling alerts operations
  """

  def set_alert(self, model: SetAlertRequestModel, key: str = None) -> SetAlertResponseModel:
    """
    Set alert

    Args:
      model (SetAlertRequestMode l): The data to be send as SetAlertRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SetAlertResponseModel: The response as SetAlertResponseModel.
    """
    response_json = self._run_request(model, endpoints.SET_ALERT, key)
    # convert the request to response model
    return SetAlertResponseModel.parse_raw(response_json)

  def cancel_alert(self, model: CancelAlertRequestModel, key: str = None) -> CancelAlertResponseModel:
    """
    Cancel alert

    Args:
      model (CancelAlertRequestModel): The data to be send as CancelAlertRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      CancelAlertResponseModel: The response as CancelAlertResponseModel.
    """
    response_json = self._run_request(model, endpoints.CANCEL_ALERT, key)
    # convert the request to response model
    return CancelAlertResponseModel.parse_raw(response_json)

  def modify_alert(self, model: ModifyAlertRequestModel, key: str = None) -> ModifyAlertResponseModel:
    """
    Modify alert

    Args:
      model (ModifyAlertRequestModel): The data to be send as ModifyAlertRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      ModifyAlertResponseModel: The response as ModifyAlertResponseModel.
    """
    response_json = self._run_request(model, endpoints.MODIFY_ALERT, key)
    # convert the request to response model
    return ModifyAlertResponseModel.parse_raw(response_json)

  def get_pending_alert(self, model: GetPendingAlertRequestModel, key: str = None) -> GetPendingAlertResponseModel:
    """
    Get pending alert

    Args:
      model (GetPendingAlertRequestModel): The data to be send as GetPendingAlertRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetPendingAlertResponseModel: The response as GetPendingAlertResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.GET_PENDING_ALERT, key)
    # convert the request to response model
    return GetPendingAlertResponseModel.parse_raw(response_json)

  def get_enabled_alert_types(self, model: GetEnabledAlertTypesRequestModel, key: str = None) -> GetEnabledAlertTypesResponseModel:
    """
    Get enabled alert types

    Args:
      model (GetEnabledAlertTypesRequestModel): The data to be send as GetEnabledAlertTypesRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetEnabledAlertTypesResponseModel: The response as GetEnabledAlertTypesResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.GET_ENABLED_ALERT_TYPES, key)
    # convert the request to response model
    return GetEnabledAlertTypesResponseModel.parse_raw(response_json)

  def place_gtt_order(self, model: PlaceGttOrderRequestModel, key: str = None) -> PlaceGttOrderResponseModel:
    """
    Place GTT order

    Args:
      model (PlaceGttOrderRequestModel): The data to be send as PlaceGttOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      PlaceGttOrderResponseModel: The response as PlaceGttOrderResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.PLACE_GTT_ORDER, key)
    # convert the request to response model
    return PlaceGttOrderResponseModel.parse_raw(response_json)

  def modify_gtt_order(self, model: ModifyGttOrderRequestModel, key: str = None) -> ModifyGttOrderResponseModel:
    """
    Modify GTT order

    Args:
      model (ModifyGttOrderRequestModel): The data to be send as ModifyGttOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      ModifyGttOrderResponseModel: The response as ModifyGttOrderResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.MODIFY_GTT_ORDER, key)
    # convert the request to response model
    return ModifyGttOrderResponseModel.parse_raw(response_json)

  def cancel_gtt_order(self, model: CancelGttOrderRequestModel, key: str = None) -> CancelGttOrderResponseModel:
    """
    Cancel GTT order

    Args:
      model (CancelGttOrderRequestModel): The data to be send as CancelGttOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      CancelGttOrderResponseModel: The response as CancelGttOrderResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.CANCEL_GTT_ORDER, key)
    # convert the request to response model
    return CancelGttOrderResponseModel.parse_raw(response_json)

  def get_pending_gtt_order(self, model: GetPendingGttOrderRequestModel, key: str = None) -> GetPendingGttOrderResponseModel:
    """
    Get pending GTT order

    Args:
      model (GetPendingGttOrderRequestModel): The data to be send as GetPendingGttOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetPendingGttOrderResponseModel: The response as GetPendingGttOrderResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.GET_PENDING_GTT_ORDER, key)
    # convert the request to response model
    return GetPendingGttOrderResponseModel.parse_raw(response_json)

  def get_enabled_gtts(self, model: GetEnabledGttsRequestModel, key: str = None) -> GetEnabledGttsResponseModel:
    """
    Get enabled GTTs

    Args:
      model (GetEnabledGttsRequestModel): The data to be send as GetEnabledGttsRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetEnabledGttsResponseModel: The response as GetEnabledGttsResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.GET_ENABLED_GTTS, key)
    # convert the request to response model
    return GetEnabledGttsResponseModel.parse_raw(response_json)

  def get_unsettled_trading_date(self, model: GetUnsettledTradingDateRequestModel, key: str = None) -> GetUnsettledTradingDateResponseModel:
    """
    Get unsettled trading date

    Args:
      model (GetUnsettledTradingDateRequestModel): The data to be send as GetUnsettledTradingDateRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetUnsettledTradingDateResponseModel: The response as GetUnsettledTradingDateResponseModel.
    """
    response_json = self._run_request(
        model, endpoints.GET_UNSETTLED_TRADING_DATE, key)
    # convert the request to response model
    return GetUnsettledTradingDateResponseModel.parse_raw(response_json)
