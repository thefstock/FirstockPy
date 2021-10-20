"""
Example usage of logout request
"""
from py_client import LogoutRequestModel
from argparse import ArgumentParser

from ..base import Example

class LogoutExample(Example):

  title: str = 'Logout'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.users.logout')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--token', type=str, help='The token recieved from login')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = LogoutRequestModel(
      uid=self.args.uid
    )
    response = self.client.logout(model, key=self.args.token)
    return [model, response]

# Run example
example = LogoutExample()
example()