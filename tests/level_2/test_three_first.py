import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(
    'items, default, result', [
        ([None], None, None),
        ([1, 2], 3, 1),
        ([1, 2], 'NOT_SET', 1),
        ((1, 2), 3, 1),
        ('12', 3, '1'),
        ('', 3, 3),
        ([], 1, 1),
        ([], None, None),
        (tuple(), 2, 2),
    ])
def test__first(items, default, result):
    assert first(items, default) == result


@pytest.mark.parametrize(
    'items, default, exception', [
        ({1, 2}, 3, TypeError),
        (3, 3, TypeError),
        ([], 'NOT_SET', AttributeError),
    ])
def test__first__exception(items, default, exception):
    with pytest.raises(exception):
        first(items, default)
