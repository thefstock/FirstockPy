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

    `exch: str`
    :   Exchange

    `uid: str`
    :   The user id of the login user

`GetIndexListResponseModel(**data: Any)`
:   The response model for get index list endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `emsg: Optional[str]`
    :   Error message if the request failed

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The get index list success or failure status

    `values: Optional[List[py_client.common.models.IndexTokenPair]]`
    :   Array Of index token pair.