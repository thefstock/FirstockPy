Module py_client.modules.funds.models.get_max_payout_amount
===========================================================
Request and response models for get max payout amount request

Classes
-------

`GetMaxPayoutAmountRequestModel(**data: Any)`
:   The request model for get max payout amount endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   The account id

    `uid: str`
    :   The user id of the login user

`GetMaxPayoutAmountResponseModel(**data: Any)`
:   The response model for get max payout amount endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `actid: Optional[str]`
    :   Account Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `payout: Optional[float]`
    :   Maximum payout amount

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The get max payout amount success or failure status