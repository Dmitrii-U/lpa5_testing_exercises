import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    'params', [
        ('Good words', {'good'}, {''}),
        ('Good words', {'good'}, {'test'}),
        ('Good words Good words', {'good'}, {''}),
        ('Good words', {'Good', 'words'}, {'test'}),
        ('Good words', {'good', 'words'}, {'words'}),
    ])
def test__check_tweet_sentiment__good(params):
    assert check_tweet_sentiment(*params) == 'GOOD'


@pytest.mark.parametrize(
    'params', [
        ('Good words', {''}, {'words'}),
        ('Good words Good words', {''}, {'words'}),
        ('Good words', {0}, {'words'}),
    ])
def test__check_tweet_sentiment__bad(params):
    assert check_tweet_sentiment(*params) == 'BAD'


@pytest.mark.parametrize(
    'params', [
        ('Good words', {'good', 'words'}, {'good', 'words'}),
        ('Good words', {'', 'words'}, {'words'}),
        ('Good words', {'Good', 'words'}, {'words'}),
        ('Good words', {'Good words'}, {'test'}),
        ('Good words', {'Good'}, {''}),
        ('Good words', {'GOOD'}, {''}),
        ('Good words', {'good'}, {'words'}),
        ('Good words', {0}, {0}),
        ('', {'good'}, {''}),
        ('', {''}, {''}),
        ('', {None}, {None}),
    ])
def test__check_tweet_sentiment__none(params):
    assert check_tweet_sentiment(*params) is None


@pytest.mark.parametrize(
    'params, exception', [
        ((None, 'good', ''), AttributeError),
        ((0, 'good', ''), AttributeError),
        (('Good words', 0, ''), TypeError),
        (('Good words', None, ''), TypeError),
    ])
def test__check_tweet_sentiment_exception(params, exception):
    with pytest.raises(exception):
        check_tweet_sentiment(*params)
