Module py_client.modules.users.datasource
=========================================
The data source for all login/logout and user requests

Classes
-------

`UserDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   The data source for all login/logout and user requests.
    
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

    `change_password(self, model: py_client.modules.users.models.change_password.ChangePasswordRequestModel) ‑> py_client.modules.users.models.change_password.ChangePasswordResponseModel`
    :   Change current password
        
        Args:
          model (ChangePasswordRequestModel): The data to be sand as ChangePasswordRequestModel
        
        Returns:
          ChangePasswordResponseModel: The response as ForgotPasswordResponseModel.

    `client_details(self, model: py_client.modules.users.models.client_details.ClientDetailsRequestModel, key: str = None) ‑> py_client.modules.users.models.client_details.ClientDetailsResponseModel`
    :   Fetch client details for the logged in user
        
        Args:
          model (ClientDetailsRequestModel): The data to be send as ClientDetailsRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ClientDetailsResponseModel: The response as ClientDetailsResponseModel.

    `forgot_password(self, model: py_client.modules.users.models.forgot_password.ForgotPasswordRequestModel) ‑> py_client.modules.users.models.forgot_password.ForgotPasswordResponseModel`
    :   Send a forgot password request to reset password
        
        Args:
          model (ForgotPasswordRequestModel): The data to be send as ForgotPasswordRequestModel.
        
        Returns:
          ForgotPasswordResponseModel: The response from forgot password request as ForgotPasswordResponseModel.

    `get_hs_token(self, model: py_client.modules.users.models.get_hs_token.GetHsTokenRequestModel, key: str = None) ‑> py_client.modules.users.models.get_hs_token.GetHsTokenResponseModel`
    :   Get one time hs token
        
        Args:
          model (GetHsTokenRequestModel): The data to be send as GetHsTokenRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetHsTokenResponseModel: The response as GetHsTokenResponseModel.

    `login(self, model: py_client.modules.users.models.login.LoginRequestModel) ‑> py_client.modules.users.models.login.LoginResponseModel`
    :   Login to the system using password or device pin.
          - If model contains the 'pwd' value login using normal login request.
          - If model contains the 'dpin' value login using device pin login request.
        
        Args:
          model (LoginRequestModel): The data to be send as LoginRequestModel.
        
        Returns:
          LoginResponseModel: The response from login request as LoginResponseModel.

    `logout(self, model: py_client.modules.users.models.logout.LogoutRequestModel, key: str = None) ‑> py_client.modules.users.models.logout.LogoutResponseModel`
    :   Logout the user
        
        Args:
          model (LogoutRequestModel): The data to be send as LogoutRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          LogoutResponseModel: The response from logout request as LogoutResponseModel.

    `save_fcm_token(self, model: py_client.modules.users.models.save_fcm_token.SaveFCMTokenRequestModel, key: str = None) ‑> py_client.modules.users.models.save_fcm_token.SaveFCMTokenResponseModel`
    :   Send request to save FCM token
        
        Args:
          model (SaveFCMTokenRequestModel): The data to be send as SaveFCMTokenRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SaveFCMTokenResponseModel: The response as SaveFCMTokenResponseModel.

    `set_device_pin(self, model: py_client.modules.users.models.set_device_pin.SetDevicePinRequestModel, key: str = None) ‑> py_client.modules.users.models.set_device_pin.SetDevicePinResponseModel`
    :   Set device pin
        
        Args:
          model (SetDevicePinRequestModel): The data to be send as SetDevicePinRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SetDevicePinResponseModel: The response as SetDevicePinResponseModel.

    `user_details(self, model: py_client.modules.users.models.user_details.UserDetailsRequestModel, key: str = None) ‑> py_client.modules.users.models.user_details.UserDetailsResponseModel`
    :   Fetch details of the logged in user
        
        Args:
          model (UserDetailsRequestModel): The data to be send as UserDetailsRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          UserDetailsResponseModel: The response as UserDetailsResponseModel.

    `validate_hs_token(self, login_id: str, token: str) ‑> bool`
    :   Check if the given HS token is valid or not
        
        Args:
          login_id (str): The sLoginId received from Initiator site,
          token (str): The HS token obtained
        
        Returns:
          bool: Whether the given token is valid or not