Module py_client.utils.decoders
===============================
Available json decorders to be used for different datatypes in models

Functions
---------

    
`build_loader(decoders: Dict[str, Callable[[Any], Any]])`
:   Build a json loader function from a map of decoders for fields that needs to be loaded differently.
    
    Args:
      decoders (Dict[str, Callable[[Any], Any]]): The docoder map

    
`datetime_decoder(transform: Callable[[datetime.datetime], Any] = None, **kwargs)`
:   Creates a datetime decoder for a given format.
    
    Args:
      kwargs: The arguments to dateutil.parser.parse method
    
    Returns:
      Callable[[str], datetime]: The datetime decoder

    
`timestamp_decoder()`
:   Creates a timestamp to datetime decoder.
    
    Returns:
      Callable[[Union[str,int]], datetime]: The datetime decoder