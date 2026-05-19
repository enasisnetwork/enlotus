"""
Functions and routines associated with Enasis Network Family Console.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Callable
from typing import Optional

from encommon.config import Params

from pydantic import Field



class LotusParams(Params, extra='forbid'):
    """
    Process and validate the core configuration parameters.
    """

    database: Annotated[
        str,
        Field('sqlite:///:memory:',
              description='Database connection string',
              min_length=1)]

    console: Annotated[
        bool,
        Field(False,
              description=(
                  'Output console information;'
                  ' parameter is parsed by and'
                  ' used in low-level config'))]

    debug: Annotated[
        bool,
        Field(False,
              description=(
                  'Enable logging level debug;'
                  ' parameter is parsed by and'
                  ' used in low-level config'))]

    dryrun: Annotated[
        bool,
        Field(False,
              description='Whether to allow changes')]

    forced: Annotated[
        bool,
        Field(True,
              description='Ignore present idempotency')]


    def __init__(
        # NOCVR
        self,
        /,
        _parse: Optional[Callable[..., Any]] = None,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """


        if _parse is not None:


            parsable = [
                'database',
                'dryrun',
                'forced']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                value = _parse(value)

                data[key] = value


        super().__init__(**data)
