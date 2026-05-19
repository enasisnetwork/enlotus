"""
Functions and routines associated with Enasis Network Family Console.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from encommon.types import DictStrAny
from encommon.utils import save_text

from pytest import fixture

from . import PROJECT
from .lotus.config import LotusConfig
from .lotus.lotus import Lotus



def config_factory(
    tmp_path: Path,
) -> LotusConfig:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    content = (
        f"""

        enconfig:
          paths:
            - {tmp_path}/lotus

        enlogger:
          stdo_level: info

        encrypts:
          phrases:
            enlotus:
              phrase: oIUc2odGYMKycATXsvXTMzxe0Qbq4z3YPPIWS8fH_uU=

        database: >-
          sqlite:///{tmp_path}/db

        """)

    config_path = (
        tmp_path / 'config.yml')

    save_text(
        config_path, content)

    sargs = {
        'config': config_path,
        'dryrun': False,
        'forced': False,
        'console': True,
        'debug': True}

    return LotusConfig(sargs)



@fixture
def config(
    tmp_path: Path,
) -> LotusConfig:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    return config_factory(tmp_path)



@fixture
def replaces(
    tmp_path: Path,
) -> DictStrAny:
    """
    Return the complete mapping of what replaced in sample.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Complete mapping of what replaced in sample.
    """

    return {
        'PROJECT': PROJECT,
        'TMPPATH': tmp_path}



def lotus_factory(
    config: LotusConfig,
) -> Lotus:
    """
    Construct the instance for use in the downstream tests.

    :param config: Primary class instance for configuration.
    :returns: Newly constructed instance of related class.
    """

    return Lotus(config)



@fixture
def lotus(
    config: LotusConfig,
) -> Lotus:
    """
    Construct the instance for use in the downstream tests.

    :param config: Primary class instance for configuration.
    :returns: Newly constructed instance of related class.
    """

    return lotus_factory(config)
