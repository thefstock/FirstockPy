Module py_client.modules.watchlists.models.search_scrips
========================================================
The request and response models for search scrip request

Classes
-------

`SearchScripsRequestModel(**data: Any)`
:   The request model for search scrip endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `stext: str`
    :   Search Text

    `exch: Optional[str]`
    :   Exchange (Select from ‘exarr’ Array provided in User Details response)

`SearchScripsResponseModel(**data: Any)`
:   The response model for search scrip endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The search scrips success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `values: List[py_client.common.models.Scrip]`
    :   Watch List names as a json array of strings.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration