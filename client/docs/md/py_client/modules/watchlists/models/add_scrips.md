Module py_client.modules.watchlists.models.add_scrips
=====================================================
The request and response models for add scrips to watchlist request

Classes
-------

`AddScripsRequestModel(**data: Any)`
:   The request model for add scrips to watchlist endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `scrips: List[str]`
    :   List of scrips

    `uid: str`
    :   The user id of the login user

    `wlname: str`
    :   Name of the Watchlist, for which scrip list is required

`AddScripsResponseModel(**data: Any)`
:   The response model for add scrips to watchlist endpoint
    
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
    :   The add scrips success or failure status