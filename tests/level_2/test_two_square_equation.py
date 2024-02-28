from math import inf

import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    'coefficients, result', [
        ((True, True, False), (-1.0, 0.0)),
        ((1, 4, 1), (-3.732050807568877, -0.2679491924311228)),
        ((-1, -4, -1), (-0.2679491924311228, -3.732050807568877)),
        ((-1, -4, 0), (0.0, -4.0)),
        ((-1, 0, 2), (1.4142135623730951, -1.4142135623730951)),
        ((-1.1, 0.1, 2.1), (1.4279005750677773, -1.3369914841586863)),
        ((0, 4, 2), (-0.5, None)),
        ((2, 0, 0), (0.0, 0.0)),
        ((0, 3, 0), (0.0, None)),
        ((0, 1, -inf), (inf, None)),
        ((2, 3, -inf), (-inf, inf)),
        ((0, inf, 1), (0.0, None)),
        ((0, -inf, 2), (0.0, None)),
    ])
def test__solve_square_equation(coefficients: tuple[int | float], result:  tuple[float, float | None]):
    assert solve_square_equation(*coefficients) == result


@pytest.mark.parametrize(
    'coefficients', [
        (True, False, True),
        (1, 2, 3),
        (-1, -2, -3),
        (0, 0, 0),
        (0, 0, 2),
        (3, 2, 1),
        (inf, 1, 1),
        (0, 0, -inf),
        (0, 0, inf),
    ])
def test__solve_square_equation__none(coefficients: tuple[int | float]):
    assert solve_square_equation(*coefficients) == (None, None)


@pytest.mark.parametrize(
    'coefficients, exception', [
        (('0', '3', '0'), TypeError),
        ((0, 3, None), TypeError),
        (([0], 3, 0), TypeError),
    ])
def test__solve_square_equation__exception(coefficients, exception: Exception()):
    with pytest.raises(exception):
        solve_square_equation(*coefficients)
