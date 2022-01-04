"""
Example of Order Book API usage
"""
from py_client import OrderBookRequestModel
from argparse import ArgumentParser

from ..base import Example

class OrderBookRequestExample(Example):

  title: str = 'Order Book'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.orders.order_book')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--token', type=str, help='The token recieved from login')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = OrderBookRequestModel(
      uid=self.args.uid
    )
    response = self.client.orders.order_book(model, key=self.args.token)
    return [model, response]

# Run example
example = OrderBookRequestExample()
example()