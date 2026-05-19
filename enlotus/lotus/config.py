"""
Functions and routines associated with Enasis Network Family Console.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Optional

from encommon.config import Config
from encommon.config import Params
from encommon.types import DictStrAny
from encommon.types import NCNone
from encommon.utils.common import PATHABLE

from .params.lotus import LotusParams



class LotusConfig(Config):
    """
    Contain the configurations from the arguments and files.

    :param sargs: Additional arguments on the command line.
    :param files: Complete or relative path to config files.
    :param cargs: Configuration arguments in dictionary form,
        which will override contents from the config files.
    """


    def __init__(
        self,
        sargs: Optional[DictStrAny] = None,
        files: Optional[PATHABLE] = None,
        cargs: Optional[DictStrAny] = None,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        sargs = dict(sargs or {})
        cargs = dict(cargs or {})


        _console = (
            sargs.get('console'))

        _debug = (
            sargs.get('debug'))

        key = 'enlogger/stdo_level'

        if _console is True:
            cargs[key] = 'info'
            cargs['console'] = True

        if _debug is True:
            cargs[key] = 'debug'
            cargs['debug'] = True


        if 'config' in sargs:
            files = sargs['config']


        _dryrun = (
            sargs.get('dryrun'))

        if _dryrun is not None:
            cargs['dryrun'] = _dryrun


        _forced = (
            sargs.get('forced'))

        if _forced is not NCNone:
            cargs['forced'] = _forced


        super().__init__(
            files=files,
            cargs=cargs,
            sargs=sargs,
            valid=LotusParams)

        self.merge_params()


    @property
    def params(
        self,
    ) -> LotusParams:
        """
        Return the Pydantic model containing the configuration.

        .. warning::
           This method completely overrides the parent but is
           based on that code, would be unfortunate if upstream
           changes meant this breaks or breaks something else.

        :returns: Pydantic model containing the configuration.
        """

        params = self.__params

        if params is not None:

            assert isinstance(
                params, LotusParams)

            return params


        basic = self.basic

        enconfig = (
            basic.get('enconfig'))

        enlogger = (
            basic.get('enlogger'))

        encrypts = (
            basic.get('encrypts'))

        basic = {
            'enconfig': enconfig,
            'enlogger': enlogger,
            'encrypts': encrypts}

        params = (
            self.valid(**basic))

        assert isinstance(
            params, LotusParams)


        self.__params = params

        return params


    def merge_params(
        self,
    ) -> None:
        """
        Update the Pydantic model containing the configuration.
        """

        merge = self.merge
        jinja2 = self.jinja2

        jinja2.set_static(
            'source', merge)

        parse = jinja2.parse

        params = self.valid(
            parse, **merge)

        assert isinstance(
            params, LotusParams)

        (jinja2
         .set_static('source'))

        self.__params = params


    @property
    def __params(
        self,
    ) -> Optional[Params]:
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        return self._Config__params


    @__params.setter
    def __params(
        self,
        value: Params | None,
    ) -> None:
        """
        Update the value for the attribute from class instance.
        """

        self._Config__params = value
