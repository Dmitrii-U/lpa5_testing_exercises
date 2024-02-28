import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    'text, replace_from, replace_to, result', [
        ('Some regular text', 'text', 'article', 'Some regular article'),
        ('Some regular text Some regular text', 'text', 'article', 'Some regular article Some regular article'),
        ('Some regular text', 'text', 'very important article', 'Some regular very important article'),
        ('Some regular text', 'regular', '', 'Some  text'),
        ('text', 'text', '', ''),
        ('text text text', 'text', '', '  '),
        ('Some regular text', 'regular text', 'abra cadabra', 'Some regular text'),
        ('', 'text', 'article', ''),
        ('Some regular text', '', 'xxx', 'Some regular text'),
        ('Some regular text', '', None, 'Some regular text'),
    ])
def test__replace_word(text: str, replace_from: str, replace_to: str, result):
    assert replace_word(text, replace_from, replace_to) == result


@pytest.mark.parametrize(
    'text, replace_from, replace_to, exception', [
        (None, 'text', 'article', AttributeError),
        (0, '', 'xxx', AttributeError),
        ('Test random words', None, 'xxx', AttributeError),
        (b'Test random words', '', 'xxx', TypeError),
        ('Test random words', 'Test', 1, TypeError),
        ('Test random words', 'Test', None, TypeError),
    ])
def test__replace_word__exception(text, replace_from, replace_to, exception: Exception()):
    with pytest.raises(exception):
        replace_word(text, replace_from, replace_to)
