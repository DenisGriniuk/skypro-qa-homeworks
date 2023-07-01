import pytest
from string_utils import StringUtils


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("skypro", "Skypro"),  # Позитивный тест: проверка первой заглавной буквы в строке
        ("", ""),  # Негативный тест: проверка первой заглавной буквы в пустой строке
        (" skypro", " skypro"),  # Негативный тест: проверка первой заглавной буквы в строке с пробелом
        ("123", "123"), # Негативный тест: проверка ввода цифр
        (None, None),  # Негативный тест: проверка первой заглавной буквы в None
    ]
)
def test_capitilize(input_string, expected_output):
    assert StringUtils().capitilize(input_string) == expected_output


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("   skypro", "skypro"),  # Позитивный тест: удаление пробелов в начале строки
        ("", ""),  # Позитивный тест: удаление пробелов в начале пустой строки
        (" skypro", "skypro"),  # Негативный тест: удаление пробелов в начале строки с пробелом
        (" 123", "123"), # Негативный тест: проверка ввода цифр
        (None, None),  # Негативный тест: удаление пробелов в начале None
    ]
)
def test_trim(input_string, expected_output):
    assert StringUtils().trim(input_string) == expected_output


@pytest.mark.parametrize(
    "input_string, delimiter, expected_output",
    [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),  # Позитивный тест: преобразование строки в список с разделителем по умолчанию
        ("1:2:3", ":", ["1", "2", "3"]),  # Позитивный тест: преобразование строки в список с пользовательским разделителем
        ("", ",", []),  # Негативный тест: преобразование пустой строки в список
        (" ", " ", [""]),  # Негативный тест: преобразование строки с пробелом в список
    ]
)
def test_to_list(input_string, delimiter, expected_output):
    assert StringUtils().to_list(input_string, delimiter) == expected_output


@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("SkyPro", "S", True),  # Позитивный тест: проверка наличия символа в строке
        ("SkyPro", "U", False),  # Позитивный тест: проверка отсутствия символа в строке
        ("", "S", False),  # Негативный тест: проверка наличия символа в пустой строке
        (" ", " ", True),  # Негативный тест: проверка наличия символа в строке с пробелом
    ]
)
def test_contains(input_string, symbol, expected_output):
    assert StringUtils().contains(input_string, symbol) == expected_output


@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("SkyPro", "k", "SyPro"),  # Позитивный тест: удаление подстроки из строки
        ("SkyPro", "Pro", "Sky"),  # Позитивный тест: удаление подстроки из строки
        ("SkyPro", "X", "SkyPro"),  # Негативный тест: удаление символа, которого нет в строке
    ]
)
def test_delete_symbol(input_string, symbol, expected_output):
    assert StringUtils().delete_symbol(input_string, symbol) == expected_output


@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("SkyPro", "S", True),  # Позитивный тест: проверка начала строки с заданным символом
        ("SkyPro", "P", False),  # Позитивный тест: проверка начала строки с отсутствующим символом
        ("", "S", False),  # Негативный тест: проверка начала пустой строки
        (" ", " ", True),  # Негативный тест: проверка начала строки с пробелом
    ]
)
def test_starts_with(input_string, symbol, expected_output):
    assert StringUtils().starts_with(input_string, symbol) == expected_output


@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("SkyPro", "o", True),  # Позитивный тест: проверка окончания строки заданным символом
        ("SkyPro", "y", False),  # Позитивный тест: проверка окончания строки отсутствующим символом
        ("", "o", False),  # Негативный тест: проверка окончания пустой строки
        (" ", " ", True),  # Негативный тест: проверка окончания строки с пробелом
    ]
)
def test_end_with(input_string, symbol, expected_output):
    assert StringUtils().end_with(input_string, symbol) == expected_output


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("", True),  # Позитивный тест: проверка пустой строки
        (" ", True),  # Позитивный тест: проверка строки, состоящей из пробелов
        ("SkyPro", False),  # Позитивный тест: проверка непустой строки
        (None, True),  # Негативный тест: проверка None
    ]
)
def test_is_empty(input_string, expected_output):
    assert StringUtils().is_empty(input_string) == expected_output


@pytest.mark.parametrize(
    "input_list, joiner, expected_output",
    [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),  # Позитивный тест: преобразование списка в строку с разделителем по умолчанию
        (["Sky", "Pro"], "-", "Sky-Pro"),  # Позитивный тест: преобразование списка в строку с пользовательским разделителем
        ([], ", ", ""),  # Негативный тест: преобразование пустого списка в строку
    ]
)
def test_list_to_string(input_list, joiner, expected_output):
    assert StringUtils().list_to_string(input_list, joiner) == expected_output
