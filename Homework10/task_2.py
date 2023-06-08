# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_no_arguments():
    with pytest.raises(IndexError):
        all_division()


@pytest.mark.smoke
def test_with_one_argument():
    assert all_division(1) == 1


@pytest.mark.smoke
def test_with_two_arguments():
    assert all_division(1, 2) == 0.5


@pytest.mark.smoke
def test_with_three_arguments():
    assert all_division(1, 2, 4) == 0.125


def test_division_by_0():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


@pytest.mark.smoke
def test_float_division1():
    assert all_division(2, 0.5) == 4


@pytest.mark.smoke
def test_float_division2():
    assert all_division(0.5, 5) == 0.1


@pytest.mark.smoke
def test_negative_value1():
    assert all_division(-5, 5) == -1


@pytest.mark.smoke
def test_negative_value_all():
    assert all_division(-5, -5) == 1

# 1. тест без аргументов
# 2. тест с 1 аргументом - [1] = 1 smoke
# 3. тест с 2 аргументом - [1,2] = 0.5 smoke
# 4. тест с 3 аргументами - [1, 2, 4] = 0.125 smoke
# 5. тест с 2 аргументами - [1, 0]
# 6. 2 арг - [2, 0.5] - 4
# 7. 2 - [0.5, 5] - 0.1
# 8. 2 - [-5, 5] - -1
# 9. 2 - [-5, -5] - 1
