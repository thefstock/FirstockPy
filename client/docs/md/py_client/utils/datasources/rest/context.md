Module py_client.utils.datasources.rest.context
===============================================
The context models required for datasource

Classes
-------

`RestContext(**data: Any)`
:   The context for RestDataSource
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `url: str`
    :

    `method: py_client.common.enums.RestMethod`
    :

    `data: Optional[str]`
    :

    `params: Dict[str, str]`
    :

    `headers: Dict[str, str]`
    :

    `result: Optional[str]`
    :

    `response: Optional[requests.models.Response]`
    :

    `Config`
    :