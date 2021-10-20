"""
The interceptor that throws proper http exceptions based on response status
"""
from typing import Dict, Type
import json

from ...common import exceptions
from ..datasources.rest.context import RestContext
from .interceptor import Interceptor

__all__ = [
  'HttpErrorInterceptor'
]

class HttpErrorInterceptor(Interceptor[RestContext]):
  """
  This interceptor throws corresponding HTTP exceptions based on response status
  """
  def __init__(self, error_msg_key: str = 'emsg') -> None:
    """
    Initialize the interceptor

    Args:
        error_msg_key (str): The key for the error message in response
    """
    self._err_msg_key = error_msg_key

  def after(self, context: RestContext) -> RestContext:
    """
    Check the response status and throw error if failed

    Args:
      context (RestContext): The context of the request
    """
    response = context.response

    switcher: Dict[int, Type[exceptions.HttpException]] = {
      400: exceptions.BadRequestError,
      401: exceptions.UnauthorizedError,
      402: exceptions.PaymentRequiredError,
      403: exceptions.ForbiddenError,
      404: exceptions.BadRequestError
    }
    # If failed
    if not response.ok:
      result: dict = json.loads(context.result)
      error_msg = result.get(self._err_msg_key)
      # Bad Request
      if response.status_code in switcher:
        raise switcher[response.status_code](response.url, msg=error_msg, headers=response.headers)
      else:
        raise exceptions.InternalServerError(response.url, msg=error_msg, headers=response.headers)
    return context