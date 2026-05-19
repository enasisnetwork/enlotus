"""
Functions and routines associated with Enasis Network Family Console.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .params.lotus import LotusParams



class LotusModels:
    """
    Return the class object that was imported within method.
    """


    @classmethod
    def lotus(
        cls,
    ) -> type['LotusParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            LotusParams)

        return LotusParams
