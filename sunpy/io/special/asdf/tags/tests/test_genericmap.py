# -*- coding: utf-8 -*-
"""
isort:skip_file
"""
import numpy as np
import pytest

import astropy.units as u
asdf = pytest.importorskip('asdf', '2.0')
from asdf.tests.helpers import assert_roundtrip_tree

import sunpy.map
from sunpy.data.test import get_test_filepath
from sunpy.io.special.asdf.extension import SunpyExtension


@pytest.fixture
def aia171_test_map():
    aia_path = get_test_filepath("aia_171_level1.fits")
    return sunpy.map.Map(aia_path)


def test_genericmap_basic(aia171_test_map, tmpdir):

    tree = {'smap': aia171_test_map}

    assert_roundtrip_tree(tree, tmpdir, extensions=SunpyExtension())


def test_genericmap_mask(aia171_test_map, tmpdir):

    mask = np.zeros_like(aia171_test_map.data)
    mask[10, 10] = 1

    aia171_test_map.mask = mask
    aia171_test_map._unit = u.m

    tree = {'smap': aia171_test_map}

    assert_roundtrip_tree(tree, tmpdir, extensions=SunpyExtension())
