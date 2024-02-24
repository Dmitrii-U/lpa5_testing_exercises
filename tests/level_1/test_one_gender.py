from functions.level_1.one_gender import genderalize


def test_genderalize(gender: dict[str, dict|str]) -> None:
    assert genderalize(**gender['param']) == gender.get('result', '')
