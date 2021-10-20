"""
Example usage of login request
"""
import uuid
import os
from py_client.common.enums import RequestSourceType
from py_client import LoginRequestModel, HttpException
from argparse import ArgumentParser
# load env files
from dotenv import load_dotenv
load_dotenv()

from ..base import Example

class LoginExample(Example):

  title: str = 'Login'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.users.login')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--pwd', type=str, help='The password for login')
    parser.add_argument('--factor2', type=str, help='The factor2 for login')
    parser.add_argument('--appkey', type=str, help='The application key')
    parser.add_argument('--dpin', type=str, help='The device pin if not using password')
    parser.add_argument('--vc', type=str, help='The vendor code')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    mac_addr = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    model = LoginRequestModel(
      apkversion= "1.0.0",
      appkey= self.args.appkey,
      vc= self.args.vc,
      uid= self.args.uid,
      pwd= self.args.pwd,
      dpin= self.args.dpin,
      factor2= self.args.factor2,
      imei= mac_addr,
      source= RequestSourceType.API
    )
    response = self.client.login(model)
    return [model, response]

# Run example
example = LoginExample()
example()