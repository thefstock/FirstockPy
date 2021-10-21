Module py_client.utils.interceptors.interceptor
===============================================
The base class for creating interceptors

Classes
-------

`Interceptor()`
:   The abstract base interceptor.
    Other interceptors should inherit from this.
    
    Args:
        C: The type of context

    ### Ancestors (in MRO)

    * typing.Generic

    ### Descendants

    * py_client.utils.interceptors.http_error.HttpErrorInterceptor

    ### Methods

    `after(self, context: ~C) ‑> ~C`
    :   This hook runs after the request is completed and the response is recieved.
        You can modify the response to transform the result.
        Augmenting the request parameters does not do anything.
        
        Args:
          context (C): The request context

    `before(self, context: ~C) ‑> ~C`
    :   This hook runs before the request is send.
        You can modify the context here to augment the request
        
        Args:
            context (C): The request context