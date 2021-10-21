Module py_client.utils.datasources.rest.datasource
==================================================
The REST data source which fetch data from rest api endpoints.

Classes
-------

`RestDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   The REST data source which fetch data from rest api endpoints.
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.stateful.Stateful

    ### Descendants

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource

    ### Methods

    `post(self, url: str, data: str, params: Dict[str, str] = {}, headers: Dict[str, str] = {}, **kwargs)`
    :   Send a post request a url and return a json response
        
        Args:
            url (str): The endpoint url
            json (str): The json payload
            params (Dict[str, str]): The query parameters
            headers (Dict[str, str]): The extra headers to pass to the request