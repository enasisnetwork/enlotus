"""
Functions and routines associated with Enasis Network Family Console.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from encommon.types import BaseModel



class ConsoParamsModel(BaseModel, extra='forbid'):
    """
    Process and validate the Conso configuration parameters.
    """
