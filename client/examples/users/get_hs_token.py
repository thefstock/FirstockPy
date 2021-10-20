"""
Example usage to retrieve HS token
"""
from py_client import GetHsTokenRequestModel
from argparse import ArgumentParser

from ..base import Example

class GetHsTokenExample(Example):

  title: str = 'Get HS Token'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.users.get_hs_token')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--token', type=str, help='The token recieved from login')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = GetHsTokenRequestModel(
      uid=self.args.uid
    )
    response = self.client.users.get_hs_token(model, key=self.args.token)
    return [model, response]

# Run example
example = GetHsTokenExample()
example()