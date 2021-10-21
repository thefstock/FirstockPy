Module py_client.modules.alerts.datasource
==========================================
Datasource for handling alerts operations

Classes
-------

`AlertsDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   Datasource for handling alerts operations
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `cancel_alert(self, model: py_client.modules.alerts.models.cancel_alert.CancelAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.cancel_alert.CancelAlertResponseModel`
    :   Cancel alert
        
        Args:
          model (CancelAlertRequestModel): The data to be send as CancelAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          CancelAlertResponseModel: The response as CancelAlertResponseModel.

    `cancel_gtt_order(self, model: py_client.modules.alerts.models.cancel_gtt_order.CancelGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.cancel_gtt_order.CancelGttOrderResponseModel`
    :   Cancel GTT order
        
        Args:
          model (CancelGttOrderRequestModel): The data to be send as CancelGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          CancelGttOrderResponseModel: The response as CancelGttOrderResponseModel.

    `get_enabled_alert_types(self, model: py_client.modules.alerts.models.get_enabled_alert_types.GetEnabledAlertTypesRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_enabled_alert_types.GetEnabledAlertTypesResponseModel`
    :   Get enabled alert types
        
        Args:
          model (GetEnabledAlertTypesRequestModel): The data to be send as GetEnabledAlertTypesRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetEnabledAlertTypesResponseModel: The response as GetEnabledAlertTypesResponseModel.

    `get_enabled_gtts(self, model: py_client.modules.alerts.models.get_enabled_gtts.GetEnabledGttsRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_enabled_gtts.GetEnabledGttsResponseModel`
    :   Get enabled GTTs
        
        Args:
          model (GetEnabledGttsRequestModel): The data to be send as GetEnabledGttsRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetEnabledGttsResponseModel: The response as GetEnabledGttsResponseModel.

    `get_pending_alert(self, model: py_client.modules.alerts.models.get_pending_alert.GetPendingAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_pending_alert.GetPendingAlertResponseModel`
    :   Get pending alert
        
        Args:
          model (GetPendingAlertRequestModel): The data to be send as GetPendingAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetPendingAlertResponseModel: The response as GetPendingAlertResponseModel.

    `get_pending_gtt_order(self, model: py_client.modules.alerts.models.get_pending_gtt_order.GetPendingGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_pending_gtt_order.GetPendingGttOrderResponseModel`
    :   Get pending GTT order
        
        Args:
          model (GetPendingGttOrderRequestModel): The data to be send as GetPendingGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetPendingGttOrderResponseModel: The response as GetPendingGttOrderResponseModel.

    `get_unsettled_trading_date(self, model: py_client.modules.alerts.models.get_unsettled_trading_date.GetUnsettledTradingDateRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_unsettled_trading_date.GetUnsettledTradingDateResponseModel`
    :   Get unsettled trading date
        
        Args:
          model (GetUnsettledTradingDateRequestModel): The data to be send as GetUnsettledTradingDateRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetUnsettledTradingDateResponseModel: The response as GetUnsettledTradingDateResponseModel.

    `modify_alert(self, model: py_client.modules.alerts.models.modify_alert.ModifyAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.modify_alert.ModifyAlertResponseModel`
    :   Modify alert
        
        Args:
          model (ModifyAlertRequestModel): The data to be send as ModifyAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ModifyAlertResponseModel: The response as ModifyAlertResponseModel.

    `modify_gtt_order(self, model: py_client.modules.alerts.models.modify_gtt_order.ModifyGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.modify_gtt_order.ModifyGttOrderResponseModel`
    :   Modify GTT order
        
        Args:
          model (ModifyGttOrderRequestModel): The data to be send as ModifyGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ModifyGttOrderResponseModel: The response as ModifyGttOrderResponseModel.

    `place_gtt_order(self, model: py_client.modules.alerts.models.place_gtt_order.PlaceGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.place_gtt_order.PlaceGttOrderResponseModel`
    :   Place GTT order
        
        Args:
          model (PlaceGttOrderRequestModel): The data to be send as PlaceGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          PlaceGttOrderResponseModel: The response as PlaceGttOrderResponseModel.

    `set_alert(self, model: py_client.modules.alerts.models.set_alert.SetAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.set_alert.SetAlertResponseModel`
    :   Set alert
        
        Args:
          model (SetAlertRequestMode l): The data to be send as SetAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SetAlertResponseModel: The response as SetAlertResponseModel.