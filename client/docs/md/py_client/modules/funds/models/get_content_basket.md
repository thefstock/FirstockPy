Module py_client.modules.funds.models.get_content_basket
========================================================
Request and response models for get content basket request

Classes
-------

`GetContentBasketRequestModel(**data: Any)`
:   The request model for get content basket endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `exch: str`
    :   Exchange Name

`GetContentBasketResponseModel(**data: Any)`
:   The response model for get content basket endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get content basket success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `basketlist: Optional[List[py_client.modules.funds.models.get_content_basket.Basket]]`
    :   List of baskets

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration

`Basket(**data: Any)`
:   Singel basket item
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `basket: str`
    :   The basket