from ast import literal_eval
from unicodedata import unidata_version

from crosshair.unicode_categories import compute_categories
from crosshair.unicode_categories import _PRECOMPUTED_CATEGORY_RANGES


def test_categories_cached_correctly():
    precomputed_str = _PRECOMPUTED_CATEGORY_RANGES[unidata_version]
    assert compute_categories() == literal_eval(precomputed_str)