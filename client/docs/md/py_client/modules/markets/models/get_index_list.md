Module py_client.modules.markets.models.get_index_list
======================================================
Request and response models for get index list request

Classes
-------

`GetIndexListRequestModel(**data: Any)`
:   The request model for get index list endpoint
    
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

`GetIndexListResponseModel(**data: Any)`
:   The response model for get index list endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get index list success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `values: Optional[List[py_client.common.models.IndexTokenPair]]`
    :   Array Of index token pair.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration