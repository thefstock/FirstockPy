Module py_client.utils.encoders
===============================
Available json encoders to be used for different datatypes in models

Functions
---------

    
`date_encoder(format: str = '%d-%m-%Y')`
:   Create a date encoder for the given format
    
    Args:
        format (str, optional): The date format. Defaults to '%d-%m-%Y'.
    
    Returns:
        Callable[[date], str]: The date encoder function

    
`list_encoder(separator: str = ',')`
:   Create a list encoder
    
    Args:
      separator (str, optional): The character used to differentiate between list items. Defaults to ','.

    
`password_hash_encoder()`
:   Create a password hash encoder
    
    Returns:
      Callable[[str], str]: The password hash encoder function