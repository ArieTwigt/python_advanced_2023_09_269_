import pytest
import math

# functions
def calc_interest(amount: float, rate: float, years: int) -> float:
    # verify the errors
    expected_types = [float, int]

    if type(amount) not in expected_types:
        raise TypeError(f"amount is of type {type(amount)}")
    
    # verify the values
    if amount < 0:
        raise ValueError(f"Amount is negative {amount}. Should be higher than 0")
    
    
    # convert the years into floor
    years_floor = math.floor(years)

    result = amount * (1 + rate) **years_floor
    
    result_rounded = round(result, 5)

    return result_rounded


# call the function
calc_interest(1000, 0.05, 0.5)

# tests
def test_calc_interest_values():
    assert calc_interest(1000, 0.05, 1) == 1050
    assert calc_interest(1000, 0.10, 1) == 1100
    assert calc_interest(1000, 0.10, 2) == 1210
    assert calc_interest(1000, 0.05, 0.5) == 1000


def test_calc_interest_wrong_data_type():
    with pytest.raises(TypeError):
        calc_interest("Arie", 0.05, 1)


def test_calc_interest_wrong_value():
    with pytest.raises(ValueError):
        calc_interest(-1000, 0.05, 1)