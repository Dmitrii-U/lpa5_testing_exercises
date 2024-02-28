import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    'github_pull_request_url', [
        'https://github.com/Dmitrii-U/lpa5_testing_exercises/pull/1',
        'https://github.com/learnpythonru/typing_challenges/pull/43'
    ])
def test__is_github_pull_request_url(github_pull_request_url: str):
    assert is_github_pull_request_url(github_pull_request_url) is True


@pytest.mark.parametrize(
    'not_github_pull_request_url', [
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'https://github.com/learnpythonru/typing_challenges/pull/43/files',
        '',
    ])
def test__is_github_pull_request_url__is_false(not_github_pull_request_url: str):
    assert is_github_pull_request_url(not_github_pull_request_url) is False


@pytest.mark.parametrize(
    'test_input, exception', [
        (None, AttributeError),
        (0, AttributeError),
    ])
def test__is_github_pull_request_url__exception(test_input, exception: Exception()):
    with pytest.raises(exception):
        is_github_pull_request_url(test_input)
