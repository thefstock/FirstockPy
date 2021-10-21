Module py_client.utils.interceptors.http_error
==============================================
The interceptor that throws proper http exceptions based on response status

Classes
-------

`HttpErrorInterceptor(error_msg_key: str = 'emsg')`
:   This interceptor throws corresponding HTTP exceptions based on response status
    
    Initialize the interceptor
    
    Args:
        error_msg_key (str): The key for the error message in response

    ### Ancestors (in MRO)

    * py_client.utils.interceptors.interceptor.Interceptor
    * typing.Generic

    ### Methods

    `after(self, context: py_client.utils.datasources.rest.context.RestContext) ‑> py_client.utils.datasources.rest.context.RestContext`
    :   Check the response status and throw error if failed
        
        Args:
          context (RestContext): The context of the request