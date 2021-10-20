import unittest
import os

from py_client import Client, ResponseStatus, RequestSourceType
from py_client.modules.users.models import *

from .common import create_login_model

class TestUserModule(unittest.TestCase):

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # login
    self.credentials = create_login_model()
    self.user = self.client.login(self.credentials)
    self.token = self.user.susertoken
    assert self.token is not None

  def test_login(self):
    """
    Test if login method is working
    """
    with self.subTest('check for valid credentials'):
      model = create_login_model()
      print(model.json())
      response = self.client.login(model)
      assert response.stat == ResponseStatus.OK
    with self.subTest('check for invalid credentials'):
      model.uid = 'ABCDEF'
      response = self.client.login(model)
      assert response.stat == ResponseStatus.NOT_OK

  def test_logout(self):
    """
    Test if logout is working
    """
    with self.subTest('should succeed with proper token and uid'):
      model = LogoutRequestModel(uid=self.credentials.uid)
      response = self.client.logout(model, key=self.token)
      assert response.stat == ResponseStatus.OK
    with self.subTest('should fail with invalid token'):
      response = self.client.logout(model, key=self.token+'somethingelse')
      assert response.stat == ResponseStatus.NOT_OK

  def test_set_device_pin(self):
    """
    Test set device pin
    """
    model = SetDevicePinRequestModel(
      uid=self.credentials.uid,
      imei='12345678',
      source=RequestSourceType.API,
      dpin='1234'
    )
    with self.subTest('should succeed for valid mpin format'):
      response = self.client.users.set_device_pin(model, self.token)
      assert response.stat == ResponseStatus.OK

    with self.subTest('should fail for valid mpin format'):
      model.dpin = 'invalid'
      response = self.client.users.set_device_pin(model, self.token)
      assert response.stat == ResponseStatus.NOT_OK

  def test_get_hs_token(self):
    """
    Test get hs token
    """
    with self.subTest('should succeed with valid user id'):
      model = GetHsTokenRequestModel(uid=self.credentials.uid)
      response = self.client.users.get_hs_token(model, self.token)
      assert response.stat == ResponseStatus.OK

    with self.subTest('should fail for invalid user id'):
      model = GetHsTokenRequestModel(uid='randomuid')
      response = self.client.users.get_hs_token(model, self.token)
      assert response.stat == ResponseStatus.NOT_OK

    with self.subTest('test for invalid key'):
      model = GetHsTokenRequestModel(uid=self.credentials.uid)
      response = self.client.users.get_hs_token(model, 'blahblah')
      assert response.stat == ResponseStatus.NOT_OK

  def test_user_details(self):
    """
    Test userdetails
    """
    with self.subTest('should succeed with passing key'):
      model = UserDetailsRequestModel(uid=self.credentials.uid)
      response = self.client.users.user_details(model, key=self.token)
      assert response.stat == ResponseStatus.OK
    with self.subTest('should succeed without passing key'):
      model = UserDetailsRequestModel(uid=self.credentials.uid)
      response = self.client.users.user_details(model)
      assert response.stat == ResponseStatus.OK
    with self.subTest('should fail with invalid user id'):
      model = UserDetailsRequestModel(uid='invalid')
      response = self.client.users.user_details(model)
      assert response.stat == ResponseStatus.NOT_OK

  def test_client_details(self):
    """
    Test client details
    """
    model = ClientDetailsRequestModel(
      uid=self.credentials.uid,
      actid=self.user.actid,
      brkname=self.user.brkname
    )
    with self.subTest('should succeed valid user id'):
      response = self.client.users.client_details(model, key=self.token)
      assert response.stat == ResponseStatus.OK
    with self.subTest('should fail invalid user id'):
      model.uid = 'invalid'
      response = self.client.users.client_details(model)
      assert response.stat == ResponseStatus.NOT_OK

  def test_save_fcm_token(self):
    """
    Test client details
    """
    model = SaveFCMTokenRequestModel(
      uid=self.credentials.uid,
      fcmtkn='123456'
    )
    with self.subTest('should succeed valid user id'):
      response = self.client.users.save_fcm_token(model)
      assert response.stat == ResponseStatus.OK
    with self.subTest('should fail invalid user id'):
      model.uid = 'invalid'
      response = self.client.users.save_fcm_token(model)
      assert response.stat == ResponseStatus.NOT_OK