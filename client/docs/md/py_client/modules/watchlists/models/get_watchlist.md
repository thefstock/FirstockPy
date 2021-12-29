Module py_client.modules.watchlists.models.get_watchlist
========================================================
The request and response models for get watchlist request

Classes
-------

`GetWatchListRequestModel(**data: Any)`
:   The request model for get watchlist endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `wlname: str`
    :   Name of the Watchlist, for which scrip list is required

`GetWatchListResponseModel(**data: Any)`
:   The response model for get watchlist endpoint
    
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
    :   The get watchlist success or failure status

    `values: List[py_client.common.models.Scrip]`
    :   Watch List names as a json array of strings.