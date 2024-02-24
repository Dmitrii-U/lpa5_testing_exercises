import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from(compose_dt_from):
    if exception := compose_dt_from.get('exception'):
        with pytest.raises(exception):
            return compose_datetime_from(**compose_dt_from['param'])
    else:
        assert compose_datetime_from(**compose_dt_from['param']).isoformat(sep=' ') == compose_dt_from['result']
