
import os
import json
import unittest
from unittest.mock import MagicMock

from py_client import Client, ResponseStatus
from py_client.models import LoginResponseModel
from py_client.modules.holdings_limits.models import *
from py_client.modules.holdings_limits import endpoints

from .common import create_login_model
from .mock import mock_post

class TestHoldingsLimits(unittest.TestCase):
  """
  Test holdings limits module
  """

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client._Client__hl.post = self.post_mock
    self.client.users.login = MagicMock(return_value=LoginResponseModel(susertoken='abcdefg'))
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None

  def test_holdings(self):
    model = HoldingsRequestModel(
      uid=self.credentials.uid,
      actid=self.credentials.uid,
      prd='ABC123'
    )
    response = self.client.holdings(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "actid": self.credentials.uid,
        "prd": 'ABC123'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.HOLDINGS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.holdqty is not None
        assert response.colqty is not None
        assert response.btstqty is not None
        assert response.btstcolqty is not None
        assert response.usedqty is not None
        assert response.upldprc is not None
        assert response.exch_tsym is not None
        assert type(response.exch_tsym) == list
        if len(response.exch_tsym) > 0:
          item = response.exch_tsym[0]
          assert item.exch is not None
          assert item.tsym is not None
          assert item.token is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_limits(self):
    model = LimitsRequestModel(
      uid=self.credentials.uid,
      actid=self.credentials.uid,
      prd='ABC123'
    )
    response = self.client.limits(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "actid": self.credentials.uid,
        "prd": 'ABC123'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.LIMITS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.cash is not None
        assert response.payin is not None
        assert response.payout is not None
        assert response.brkcollamt is not None
        assert response.unclearedcash is not None
        assert response.daycash is not None
        assert response.turnoverlmt is not None
        assert response.pendordvallmt is not None
        assert response.turnover is not None
        assert response.pendordval is not None
        assert response.marginused is not None
        assert response.mtomcurper is not None
        assert response.unmtom is not None
        assert response.grexpo is not None
        assert response.uzpnl_e_i is not None
        assert response.uzpnl_e_m is not None
        assert response.uzpnl_e_c is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
