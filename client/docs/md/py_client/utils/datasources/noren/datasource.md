Module py_client.utils.datasources.noren.datasource
===================================================
Data sources for noren requests

Classes
-------

`NorenRestDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   The rest datasource for noren apis
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Descendants

    * py_client.modules.alerts.datasource.AlertsDataSource
    * py_client.modules.funds.datasource.FundsDataSource
    * py_client.modules.holdings_limits.datasource.HoldingsLimitsDataSource
    * py_client.modules.markets.datasource.MarketsDataSource
    * py_client.modules.orders.datasource.OrdersDataSource
    * py_client.modules.users.datasource.UserDataSource
    * py_client.modules.watchlists.datasource.WatchListDataSource