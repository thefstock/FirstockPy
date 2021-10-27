
import os
import json
import unittest
from unittest.mock import MagicMock

from py_client import Client, ResponseStatus
from py_client.models import LoginResponseModel
from py_client.modules.funds.models import *
from py_client.modules.funds import endpoints

from .common import create_login_model
from .mock import mock_post

class TestFunds(unittest.TestCase):
  """
  Test funds module
  """

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client.funds.post = self.post_mock
    self.client.users.login = MagicMock(return_value=LoginResponseModel(susertoken='abcdefg'))
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None

  def test_get_max_payout_amount(self):
    model = GetMaxPayoutAmountRequestModel(
      uid=self.credentials.uid,
      actid=self.credentials.uid
    )
    response = self.client.funds.get_max_payout_amount(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "actid": self.credentials.uid}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_MAX_PAYOUT_AMOUNT, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.actid is not None
        assert response.payout is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_content_basket(self):
    model = GetContentBasketRequestModel(
      uid=self.credentials.uid,
      exch="NSE"
    )
    response = self.client.funds.get_content_basket(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "exch": "NSE"}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_CONTENT_BASKET, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.basketlists is not None
        assert type(response.basketlists) == list
        if len(response.basketlists) > 0:
          basket = response.basketlists[0]
          assert basket is not None
          assert basket.basket is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_content_list(self):
    model = GetContentListRequestModel(
      uid=self.credentials.uid,
      exch='NSE',
      condition_name='UpperCircuit',
      basket='BSEEQ'
    )
    response = self.client.funds.get_content_list(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid":self.credentials.uid,
        "exch":'NSE',
        "condition_name":'UpperCircuit',
        "basket":'BSEEQ'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_CONTENT_LIST, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.tsym is not None
        assert response.lp is not None
        assert response.c is not None
        assert response.h is not None
        assert response.l is not None
        assert response.ap is not None
        assert response.v is not None
        assert response.ltt is not None
        assert response.pc is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
