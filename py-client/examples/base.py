"""
The base class for running examples
"""

from abc import ABC, abstractclassmethod
from typing import Tuple
from pydantic.main import BaseModel
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from py_client import Client, HttpException

class Example(ABC):

  title: str = 'Example'

  def __init__(self) -> None:
    # base_url = 'https://norenapi.thefirstock.com/NorenWClient'
    base_url = 'https://rama.kambala.co.in/NorenWClientTP/'
    self.client = Client(api_url=base_url)
    self.parse_args()

  def print_output(self, payload: str, response: str, title: str = 'JSON'):
    """
    Print rich json output
    """
    console = Console()
    payload = Syntax(payload, "json", word_wrap=True)
    response = Syntax(response, "json", word_wrap=True)
    table = Table(title=title, show_header=True, header_style="bold magenta")
    table.add_column('Payload')
    table.add_column('Response')
    table.add_row(payload, response)
    console.print(table)

  def __call__(self) -> None:
    try:
      [model, response] = self.run()
      payload = model.json(exclude_unset=True, indent=2)
      output =  response.json(exclude_unset=True, indent=2)
      self.print_output(payload, output, self.title)
    except HttpException as e:
      print(e.reason)
    except Exception as e:
      print(e)

  @abstractclassmethod
  def parse_args(self):
    pass

  @abstractclassmethod
  def run(self) -> Tuple[BaseModel, BaseModel]:
    pass