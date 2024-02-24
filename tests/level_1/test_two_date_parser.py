from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from(compose_dt_from):
    assert compose_datetime_from(**compose_dt_from['param']) == compose_dt_from['result']
