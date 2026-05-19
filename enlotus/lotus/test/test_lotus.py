"""
Functions and routines associated with Enasis Network Family Console.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from encommon.types import DictStrAny
from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs
from encommon.utils import load_sample
from encommon.utils import prep_sample
from encommon.utils.sample import ENPYRWS

from . import SAMPLES
from ..config import LotusConfig
from ..lotus import Lotus



def test_Lotus(
    lotus: Lotus,
    replaces: DictStrAny,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param lotus: Primary class instance for Family Console.
    :param replaces: Mapping of what to replace in samples.
    """


    attrs = lattrs(lotus)

    assert attrs == [
        '_Lotus__config']


    assert inrepr(
        'lotus.Lotus',
        lotus)

    assert isinstance(
        hash(lotus), int)

    assert instr(
        'lotus.Lotus',
        lotus)


    assert lotus.config

    assert lotus.params

    assert lotus.console

    assert lotus.debug

    assert not lotus.dryrun

    assert not lotus.forced


    sample_path = (
        SAMPLES / 'dumped.json')

    sample = load_sample(
        path=sample_path,
        update=ENPYRWS,
        content=lotus.dumped,
        replace=replaces)

    expect = prep_sample(
        content=lotus.dumped,
        replace=replaces)

    assert expect == sample



def test_Lotus_cover(
) -> None:
    """
    Perform various tests associated with relevant routines.
    """

    Lotus(LotusConfig())
