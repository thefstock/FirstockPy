Module py_client.common.exceptions
==================================
Custom exceptions for http requests

Classes
-------

`BadRequestError(url: str, msg: str = None, headers: Any = {})`
:   The http error corresponding to 400 status code
    
    Initialize a BadRequestError

    ### Ancestors (in MRO)

    * py_client.common.exceptions.HttpException
    * urllib.error.HTTPError
    * urllib.error.URLError
    * builtins.OSError
    * builtins.Exception
    * builtins.BaseException
    * urllib.response.addinfourl
    * urllib.response.addinfo
    * urllib.response.addbase
    * tempfile._TemporaryFileWrapper

`ForbiddenError(url: str, msg: str = None, headers: Any = {})`
:   The http error corresponding to 403 status code
    
    Initialize a BadRequestError

    ### Ancestors (in MRO)

    * py_client.common.exceptions.HttpException
    * urllib.error.HTTPError
    * urllib.error.URLError
    * builtins.OSError
    * builtins.Exception
    * builtins.BaseException
    * urllib.response.addinfourl
    * urllib.response.addinfo
    * urllib.response.addbase
    * tempfile._TemporaryFileWrapper

`HttpException(url: str, code: http.HTTPStatus, msg: str, headers={})`
:   The base http exception class

    ### Ancestors (in MRO)

    * urllib.error.HTTPError
    * urllib.error.URLError
    * builtins.OSError
    * builtins.Exception
    * builtins.BaseException
    * urllib.response.addinfourl
    * urllib.response.addinfo
    * urllib.response.addbase
    * tempfile._TemporaryFileWrapper

    ### Descendants

    * py_client.common.exceptions.BadRequestError
    * py_client.common.exceptions.ForbiddenError
    * py_client.common.exceptions.InternalServerError
    * py_client.common.exceptions.NotFoundError
    * py_client.common.exceptions.PaymentRequiredError
    * py_client.common.exceptions.UnauthorizedError

`InternalServerError(url: str, msg: str = None, headers: Any = {})`
:   The http error corresponding to 500 status code
    
    Initialize a BadRequestError

    ### Ancestors (in MRO)

    * py_client.common.exceptions.HttpException
    * urllib.error.HTTPError
    * urllib.error.URLError
    * builtins.OSError
    * builtins.Exception
    * builtins.BaseException
    * urllib.response.addinfourl
    * urllib.response.addinfo
    * urllib.response.addbase
    * tempfile._TemporaryFileWrapper

`NotFoundError(url: str, msg: str = None, headers: Any = {})`
:   The http error corresponding to 404 status code
    
    Initialize a BadRequestError

    ### Ancestors (in MRO)

    * py_client.common.exceptions.HttpException
    * urllib.error.HTTPError
    * urllib.error.URLError
    * builtins.OSError
    * builtins.Exception
    * builtins.BaseException
    * urllib.response.addinfourl
    * urllib.response.addinfo
    * urllib.response.addbase
    * tempfile._TemporaryFileWrapper

`PaymentRequiredError(url: str, msg: str = None, headers: Any = {})`
:   The http error corresponding to 402 status code
    
    Initialize a BadRequestError

    ### Ancestors (in MRO)

    * py_client.common.exceptions.HttpException
    * urllib.error.HTTPError
    * urllib.error.URLError
    * builtins.OSError
    * builtins.Exception
    * builtins.BaseException
    * urllib.response.addinfourl
    * urllib.response.addinfo
    * urllib.response.addbase
    * tempfile._TemporaryFileWrapper

`UnauthorizedError(url: str, msg: str = None, headers: Any = {})`
:   The http error corresponding to 401 status code
    
    Initialize a BadRequestError

    ### Ancestors (in MRO)

    * py_client.common.exceptions.HttpException
    * urllib.error.HTTPError
    * urllib.error.URLError
    * builtins.OSError
    * builtins.Exception
    * builtins.BaseException
    * urllib.response.addinfourl
    * urllib.response.addinfo
    * urllib.response.addbase
    * tempfile._TemporaryFileWrapper