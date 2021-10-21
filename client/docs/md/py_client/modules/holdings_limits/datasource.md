Module py_client.modules.holdings_limits.datasource
===================================================
Datasource for handling holdings_limits operations

Classes
-------

`HoldingsLimitsDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   Datasource for handling holdings_limits operations
    
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

    `holdings(self, model: py_client.modules.holdings_limits.models.holdings.HoldingsRequestModel, key: str = None) ‑> py_client.modules.holdings_limits.models.holdings.HoldingsResponseModel`
    :   Holdings
        
        Args:
          model (HoldingsRequestModel): The data to be send as HoldingsRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          HoldingsResponseModel: The response as HoldingsResponseModel.

    `limits(self, model: py_client.modules.holdings_limits.models.limits.LimitsRequestModel, key: str = None) ‑> py_client.modules.holdings_limits.models.limits.LimitsResponseModel`
    :   Limits
        
        Args:
          model (LimitsRequestModel): The data to be send as LimitsRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          LimitsResponseModel: The response as LimitsResponseModel.