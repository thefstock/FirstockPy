Module py_client.client
=======================
The client combines all the modules and abstracts the inner logic

Classes
-------

`Client(api_url: str, socket_url: str)`
:   The python client for communicating with external api
    
    Initialize the client
    
    Args:
      base_url (str, optional): The base url for the rest api endpoint. Defaults to None.

    ### Ancestors (in MRO)

    * py_client.utils.stateful.Stateful

    ### Instance variables

    `alerts: py_client.modules.alerts.datasource.AlertsDataSource`
    :   The alerts module datasource

    `funds: py_client.modules.funds.datasource.FundsDataSource`
    :   The funds module datasource

    `markets: py_client.modules.markets.datasource.MarketsDataSource`
    :   The markets module datasource

    `orders: py_client.modules.orders.datasource.OrdersDataSource`
    :   The orders module datasource

    `state`
    :   The current client state

    `users: py_client.modules.users.datasource.UserDataSource`
    :   The user module datasource

    `watchlists: py_client.modules.watchlists.datasource.WatchListDataSource`
    :   The watchlists module datasource

    `ws`
    :   The websocket client

    ### Methods

    `holdings(self, model: py_client.modules.holdings_limits.models.holdings.HoldingsRequestModel, key: str)`
    :   Get holdings
        
        Args:
          model (HoldingsRequestModel): The data to be send as HoldingsRequestModel.
          key (str): The key obtained on login success
        
        Returns:
          HoldingsResponseModel: The response as HoldingsResponseModel.

    `limits(self, model: py_client.modules.holdings_limits.models.limits.LimitsRequestModel, key: str = None)`
    :   Limits
        
        Args:
          model (LimitsRequestModel): The data to be send as LimitsRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          LimitsResponseModel: The response as LimitsResponseModel.

    `login(self, model: py_client.modules.users.models.login.LoginRequestModel)`
    :   Login user. Alias for ```client.users.login```
        
        Args:
          model (LoginRequestModel): The data to be send as LoginRequestModel instance.
        
        Returns:
          LoginResponseModel: The response from login request as LoginResponseModel instance.

    `logout(self, model: py_client.modules.users.models.logout.LogoutRequestModel, key: str = None)`
    :   Logout user. Alias for ```client.users.logout```
        
        Args:
          model (LogoutRequestModel): The data to be send as LogoutRequestModel instance
          key (str): The key obtained on login success
        
        Returns:
          LogoutResponseModel: The response from logout request as LogoutResponseModel instance