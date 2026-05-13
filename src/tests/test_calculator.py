"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

# TODO: ajoutez les tests
def test_addition():
    # Test case : 2 positives  integer values
    my_calculator = Calculator()
    res = my_calculator.addition(2, 3)
    assert res == 5

def test_addition():
    # Test case : 2 positives  integer values
    my_calculator = Calculator()
    res = my_calculator.addition(2, 3)
    assert res == 5

def test_soustraction():
    # Test case : 2 positives  integer values
    my_calculator = Calculator()
    res = my_calculator.subtraction(10,8)
    assert res == 2

def test_addition():
    # Test case : 2 positives  integer values
    my_calculator = Calculator()
    res = my_calculator.multiplication(2, 3)
    assert res == 6

def test_addition():
    # Test case : 2 positives  integer values
    my_calculator = Calculator()
    res = my_calculator.division(50,2)
    assert res == 25
