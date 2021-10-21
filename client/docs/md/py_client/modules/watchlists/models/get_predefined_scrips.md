Module py_client.modules.watchlists.models.get_predefined_scrips
================================================================
The request and response models for get predefined scrips request

Classes
-------

`GetPredefinedScripsRequestModel(**data: Any)`
:   The request model for get predefined scrips endpoint
    
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

`GetPredefinedScripsResponseModel(**data: Any)`
:   The response model for get predefined scrips endpoint
    
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
    :   The get predefined scrips success or failure status

    `values: List[py_client.common.models.Scrip]`
    :   Watch List names as a json array of strings.