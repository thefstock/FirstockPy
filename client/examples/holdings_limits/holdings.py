"""
Example of Holdings API usage
"""
from py_client import HoldingsRequestModel
from argparse import ArgumentParser

from ..base import Example

class HoldingsRequestExample(Example):

  title: str = 'Holdings'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.holdings_limits.holdings')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--token', type=str, help='The token recieved from login')
    parser.add_argument('--actid', type=str, help='The Account Id of the logged in user')
    parser.add_argument('--prd', type=str, help='The Product Name')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = HoldingsRequestModel(
      uid=self.args.uid,
      actid=self.args.actid,
      prd=self.args.prd
    )
    response = self.client.holdings(model, key=self.args.token)
    return [model, response]

# Run example
example = HoldingsRequestExample()
example()