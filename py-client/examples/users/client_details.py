"""
Example usage of logout request
"""
from py_client import ClientDetailsRequestModel
from argparse import ArgumentParser

from ..base import Example

class ClientDetailsExample(Example):

  title: str = 'Client Details'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.users.logout')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--actid', type=str, help='The account id')
    parser.add_argument('--brkname', type=str, help='The broker id')
    parser.add_argument('--token', type=str, help='The token recieved from login')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = ClientDetailsRequestModel(
      uid=self.args.uid,
      actid=self.args.actid,
      brkname=self.args.brkname
    )
    response = self.client.users.client_details(model, key=self.args.token)
    return [model, response]

# Run example
example = ClientDetailsExample()
example()