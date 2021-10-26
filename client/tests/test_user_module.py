import os
import json
import unittest
import pytest
from datetime import date, datetime
from unittest.mock import MagicMock

from py_client import Client, ResponseStatus, RequestSourceType
from py_client.modules.users.models import *
from py_client.modules.users import endpoints

from .common import create_login_model
from .mock import mock_post

class TestUserModule(unittest.TestCase):

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client.users.post = self.post_mock
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None

  def test_login(self):
    """
    Test if login method is working
    """
    model = LoginRequestModel(
      apkversion = '1.0',
      uid = 'ABC123',
      pwd = 'SECRET',
      factor2 = "AEIEOP382",
      vc = '123456',
      appkey = 'abcdefg12345',
      imei = "134243434",
      source = RequestSourceType.API
    )
    response = self.client.login(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "apkversion":'1.0',
        "uid": "ABC123",
        "pwd": "0917b13a9091915d54b6336f45909539cce452b3661b21f386418a257883b30a",
        "factor2": "AEIEOP382",
        "vc":'123456',
        "appkey":'abcdefg12345',
        "imei":"134243434",
        "source": "API"
      }
      expected_body = f'jData={json.dumps(expected_data)}'
      self.post_mock.assert_called_with(endpoints.LOGIN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.susertoken is not None
        assert type(response.susertoken) == str
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_login_dpin(self):
    """
    Test if login method with dpin is working
    """
    model = LoginRequestModel(
      apkversion = '1.0',
      uid = 'ABC123',
      dpin = 'SECRET',
      factor2 = "AEIEOP382",
      vc = '123456',
      appkey = 'abcdefg12345',
      imei = "134243434",
      source = RequestSourceType.API
    )
    response = self.client.login(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "apkversion":'1.0',
        "uid": "ABC123",
        "dpin": "0917b13a9091915d54b6336f45909539cce452b3661b21f386418a257883b30a",
        "factor2": "AEIEOP382",
        "vc":'123456',
        "appkey":'abcdefg12345',
        "imei":"134243434",
        "source": "API"
      }
      expected_body = f'jData={json.dumps(expected_data)}'
      self.post_mock.assert_called_with(endpoints.LOGIN_WITH_DPIN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.susertoken is not None
        assert type(response.susertoken) == str
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_logout(self):
    """
    Test if logout is working
    """
    model = LogoutRequestModel(uid=self.credentials.uid)
    response = self.client.logout(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.LOGOUT, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_forgot_password(self):
    """
    Test forgot password
    """
    model = ForgotPasswordRequestModel(uid=self.credentials.uid, pan='AEIAPP28282', dob=date(1998,4,28))
    response = self.client.users.forgot_password(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid, "pan": 'AEIAPP28282', "dob": "28-04-1998" }
      expected_body = f'jData={json.dumps(expected_data)}'
      self.post_mock.assert_called_with(endpoints.FORGOT_PASSWORD, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_change_password(self):
    """
    Test change password
    """
    model = ChangePasswordRequestModel(uid=self.credentials.uid, oldpwd='SECRET', pwd='NEWSECRET')
    response = self.client.users.change_password(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "oldpwd": '0917b13a9091915d54b6336f45909539cce452b3661b21f386418a257883b30a',
        "pwd": "NEWSECRET"
      }
      expected_body = f'jData={json.dumps(expected_data)}'
      self.post_mock.assert_called_with(endpoints.CHANGE_PASSWORD, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.dmsg is not None
        assert type(response.dmsg) == str
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

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
    response = self.client.users.set_device_pin(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid, "imei": '12345678', "source": "API", "dpin": "1234" }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.SET_DEVICE_PIN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
  
  @pytest.mark.skip(reason = 'No sample response available')
  def test_get_hs_token(self):
    """
    Test get hs token
    """
    model = GetHsTokenRequestModel(uid=self.credentials.uid)
    response = self.client.users.get_hs_token(model, self.token)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_HS_TOKEN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_validate_hs_token(self):
    """
    Test get hs token
    """
    response = self.client.users.validate_hs_token('ABC123', 'fa2356ba58ccd56efd66d')
    with self.subTest('request should be called with proper data'):
      expected_body = "LoginId=ABC123&token=fa2356ba58ccd56efd66d"
      self.post_mock.assert_called_with(endpoints.VERIFY_HS_TOKEN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert type(response) == bool

  def test_user_details(self):
    """
    Test user details
    """
    model = UserDetailsRequestModel(uid=self.credentials.uid)
    response = self.client.users.user_details(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.USER_DETAILS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.brkname is not None
        assert response.email is not None
        assert response.actid is not None
        assert response.prarr is not None
        assert type(response.prarr) == list
        assert response.orarr is not None
        assert type(response.orarr) == list
        assert response.exarr is not None
        assert type(response.exarr) == list
        if len(response.prarr) > 0:
          product = response.prarr[0]
          assert product is not None
          assert product.prd is not None
          assert product.s_prdt_ali is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  @pytest.mark.skip(reason = 'No sample response available')
  def test_client_details(self):
    """
    Test client details
    """
    model = ClientDetailsRequestModel(uid=self.credentials.uid, actid=self.credentials.uid, brkname='ABCD')
    response = self.client.users.client_details(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid, "actid": self.credentials.uid, "brkname": 'ABCD' }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.CLIENT_DETAILS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.email is not None
        assert response.actid is not None
        assert response.bankdetails is not None
        assert type(response.bankdetails) == list
        assert response.dp_acct_num is not None
        assert type(response.dp_acct_num) == list
        if len(response.bankdetails) > 0:
          details = response.bankdetails[0]
          assert details is not None
          assert details.bankn is not None
          assert details.acctnum is not None
        if len(response.dp_acct_num) > 0:
          acc = response.dp_acct_num[0]
          assert acc is not None
          assert acc.dpnum is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_save_fcm_token(self):
    """
    Test save fcm token
    """
    model = SaveFCMTokenRequestModel(uid=self.credentials.uid, fcmtkn='abcd12345')
    response = self.client.users.save_fcm_token(model, self.token)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid, "fcmtkn": 'abcd12345' }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.SAVE_FCM_TOKEN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str