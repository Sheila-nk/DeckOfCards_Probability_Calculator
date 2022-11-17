import pytest
import probability_calculator
import sys, io

@pytest.mark.parametrize("configuration, probability",
[
    (["3"], 0.0769),
    (["3H"], 0.0192),
    (["H"], 0.2500),
]
)
def test_probability_of_picking_one_card(configuration, probability):
    assert probability_calculator.probability_calc(configuration) == probability

@pytest.mark.parametrize("configuration, order, probability",
[
    (["3H", "4S", "9C"], "Y", 132600.0),
    (["3H", "4S", "9C"], "N", 22100.0),
    (["K", "H", "3S"], "Y", 2.7320194583164843e+29),
    (["K", "H", "3S"], "N", 42671977361650.0),
]
)
def test_probability_of_picking_multiple_cards(configuration, order, probability):
    sys.stdin = io.StringIO(order)
    assert probability_calculator.probability_calc(configuration) == probability

def test_error_message_and_exceptions(capsys):
    config_list = ["3KG, X, 11"]
    result = probability_calculator.checker(config_list)
    out, err = capsys.readouterr()
    assert out.startswith("Wrong Usage!")
    assert result == False

def test_empty_list(capsys):
    empty_list = []
    result = probability_calculator.checker(empty_list)
    out, err = capsys.readouterr()
    assert out.startswith("Wrong Usage!")
    assert result == False