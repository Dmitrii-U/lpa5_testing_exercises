from functions.level_1.one_gender import genderalize


def test_genderalize(gender: dict[str, str]) -> None:
    assert genderalize(**gender['param']) == gender['result']
