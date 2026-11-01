import allure

from typing import Any

@allure.step('Check that response status code equals to {expected}')
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, f'Incorrect response status code. Expected status code: {expected}. Actual status code: {actual}'

@allure.step('Check that {name} equals to {expected}')
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, f'Incorrect value: "{name}". Expected value: {expected}. Actual value: {actual}'

@allure.step('Check that {name} is true')
def assert_is_true(actual: Any, name: str):
    assert actual, f'Incorrect value: "{name}". Expected true value but got: {actual}'
from typing import Sized

def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    with allure.step(f'Check that length of {name} equals to {len(expected)}'):
        assert len(actual) == len(expected), f'Incorrect object length: "{name}". Expected length: {len(expected)}. Actual length: {len(actual)}'
