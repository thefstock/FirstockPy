Module py_client.modules.markets.models.top_list_names
======================================================
Request and response models for top list names request

Classes
-------

`TopListNamesRequestModel(**data: Any)`
:   The request model for top list names endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `exch: str`
    :   Exchange

`TopListNamesResponseModel(**data: Any)`
:   The response model for top list names endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The top list names success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `values: Optional[List[py_client.common.models.BasketCriteriaPair]]`
    :   Array of Basket, Criteria pair

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration