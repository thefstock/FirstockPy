Module py_client.modules.users.models.set_device_pin
====================================================
Request and response models for set device pin

Classes
-------

`SetDevicePinRequestModel(**data: Any)`
:   The data model for set device pin request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   User Id

    `imei: str`
    :   IMEI or device unique fingerprint

    `source: py_client.common.enums.RequestSourceType`
    :   Access type

    `dpin: str`
    :   New pin

`SetDevicePinResponseModel(**data: Any)`
:   The data model for set device pin response
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The set device pin success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful setting of new pin.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration