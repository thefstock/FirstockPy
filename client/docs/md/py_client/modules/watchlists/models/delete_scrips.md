Module py_client.modules.watchlists.models.delete_scrips
========================================================
The request and response models for delete scrips from watchlist request

Classes
-------

`DeleteScripsRequestModel(**data: Any)`
:   The request model for delete scrips from watchlist endpoint
    
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

    `scrips: List[str]`
    :   List of scrips

    `Config`
    :   model configuration

`DeleteScripsResponseModel(**data: Any)`
:   The response model for delete scrips from watchlist endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The delete scrips success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration