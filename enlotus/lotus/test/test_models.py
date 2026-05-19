"""
Functions and routines associated with Enasis Network Family Console.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..models import LotusModels



def test_LotusModels_cover() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    models = LotusModels

    assert models.lotus()
