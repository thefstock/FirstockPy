Module py_client.modules.markets.models.top_list
================================================
Request and response models for top list request

Classes
-------

`TopListRequestModel(**data: Any)`
:   The request model for top list endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `bskt: str`
    :   Basket name

    `crt: str`
    :   Criteria

    `exch: str`
    :   Exchange

    `tb: str`
    :   T or B Top or Bottom

    `uid: str`
    :   The user id of the login user

`TopListResponseModel(**data: Any)`
:   The response model for top list endpoint
    
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
    :   The top list success or failure status

    `values: Optional[List[py_client.common.models.TBContract]]`
    :   Array of top / bottom contracts object