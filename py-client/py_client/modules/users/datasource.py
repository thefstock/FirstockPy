"""
The data source for all login/logout and user requests
"""

from ...utils.datasources import NorenRestDataSource
from . import endpoints

from .models import *

class UserDataSource(NorenRestDataSource):
  """
  The data source for all login/logout and user requests.
  """

  def login(self, model: LoginRequestModel) -> LoginResponseModel:
    """
    Login to the system using password or device pin.
      - If model contains the 'pwd' value login using normal login request.
      - If model contains the 'dpin' value login using device pin login request.

    Args:
      model (LoginRequestModel): The data to be send as LoginRequestModel.

    Returns:
      LoginResponseModel: The response from login request as LoginResponseModel.
    """
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # get the endpint based on secret provided
    url = endpoints.LOGIN if model.pwd is not None else endpoints.LOGIN_WITH_DPIN
    # send the post request to get the json response
    response_json = self.post(url, f"jData={request_json}")
    # convert the request to response model
    return LoginResponseModel.parse_raw(response_json)

  def logout(self, model: LogoutRequestModel, key: str = None) -> LogoutResponseModel:
    """
    Logout the user

    Args:
      model (LogoutRequestModel): The data to be send as LogoutRequestModel.
      key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      LogoutResponseModel: The response from logout request as LogoutResponseModel.
    """
    response_json = self._run_request(model, endpoints.LOGOUT, key)
    # convert the request to response model
    return LogoutResponseModel.parse_raw(response_json)

  def forgot_password(self, model: ForgotPasswordRequestModel) -> ForgotPasswordResponseModel:
    """
    Send a forgot password request to reset password

    Args:
      model (ForgotPasswordRequestModel): The data to be send as ForgotPasswordRequestModel.

    Returns:
      ForgotPasswordResponseModel: The response from forgot password request as ForgotPasswordResponseModel.
    """
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.FORGOT_PASSWORD, f"jData={request_json}")
    # convert the request to response model
    return ForgotPasswordResponseModel.parse_raw(response_json)

  def change_password(self, model: ChangePasswordRequestModel) -> ChangePasswordResponseModel:
    """
    Change current password

    Args:
      model (ChangePasswordRequestModel): The data to be sand as ChangePasswordRequestModel

    Returns:
      ChangePasswordResponseModel: The response as ForgotPasswordResponseModel.
    """
    # convert request model to json string
    request_json = model.json(exclude_unset=True)
    # send the post request to get the json response
    response_json = self.post(endpoints.CHANGE_PASSWORD, f"jData={request_json}")
    # convert the request to response model
    return ChangePasswordResponseModel.parse_raw(response_json)

  def set_device_pin(self, model: SetDevicePinRequestModel, key: str = None) -> SetDevicePinResponseModel:
    """
    Set device pin

    Args:
      model (SetDevicePinRequestModel): The data to be send as SetDevicePinRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SetDevicePinResponseModel: The response as SetDevicePinResponseModel.
    """
    response_json = self._run_request(model, endpoints.SET_DEVICE_PIN, key)
    # convert the request to response model
    return SetDevicePinResponseModel.parse_raw(response_json)

  def get_hs_token(self, model: GetHsTokenRequestModel, key: str = None) -> GetHsTokenResponseModel:
    """
    Get one time hs token

    Args:
      model (GetHsTokenRequestModel): The data to be send as GetHsTokenRequestModel
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetHsTokenResponseModel: The response as GetHsTokenResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_HS_TOKEN, key)
    # convert the request to response model
    return GetHsTokenResponseModel.parse_raw(response_json)

  def validate_hs_token(self, login_id: str, token: str) -> bool:
    """
    Check if the given HS token is valid or not

    Args:
      login_id (str): The sLoginId received from Initiator site,
      token (str): The HS token obtained

    Returns:
      bool: Whether the given token is valid or not
    """
    # send the post request to get the text response
    response = self.post(endpoints.VERIFY_HS_TOKEN, f"LoginId={login_id}&token={token}")
    # convert the response text to boolean
    return response.strip() == 'TRUE'

  def user_details(self, model: UserDetailsRequestModel, key: str = None) -> UserDetailsResponseModel:
    """
    Fetch details of the logged in user

    Args:
      model (UserDetailsRequestModel): The data to be send as UserDetailsRequestModel
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      UserDetailsResponseModel: The response as UserDetailsResponseModel.
    """
    response_json = self._run_request(model, endpoints.USER_DETAILS, key)
    # convert the request to response model
    return UserDetailsResponseModel.parse_raw(response_json)

  def client_details(self, model: ClientDetailsRequestModel, key: str = None) -> ClientDetailsResponseModel:
    """
    Fetch client details for the logged in user

    Args:
      model (ClientDetailsRequestModel): The data to be send as ClientDetailsRequestModel
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      ClientDetailsResponseModel: The response as ClientDetailsResponseModel.
    """
    response_json = self._run_request(model, endpoints.CLIENT_DETAILS, key)
    # convert the request to response model
    return ClientDetailsResponseModel.parse_raw(response_json)

  def save_fcm_token(self, model: SaveFCMTokenRequestModel, key: str = None) -> SaveFCMTokenResponseModel:
    """
    Send request to save FCM token

    Args:
      model (SaveFCMTokenRequestModel): The data to be send as SaveFCMTokenRequestModel
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SaveFCMTokenResponseModel: The response as SaveFCMTokenResponseModel.
    """
    response_json = self._run_request(model, endpoints.SAVE_FCM_TOKEN, key)
    # convert the request to response model
    return SaveFCMTokenResponseModel.parse_raw(response_json)