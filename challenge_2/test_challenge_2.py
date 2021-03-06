# Coding Challenge #2 Test Suite
from challenge_2 import transpose


def test_empty_string():
    input_value = ""
    expected = ""
    assert expected == transpose(input_value)


def test_two_characters_in_a_row():
    input_value = "A1"
    expected = "A\n1"
    assert expected == transpose(input_value)


def test_simple():
    input_value = "ABC\n123"
    expected = "A1\nB2\nC3"
    assert expected == transpose(input_value)


def test_square():
    input_value = "HEART\nEMBER\nABUSE\nRESIN\nTREND"
    expected = "HEART\nEMBER\nABUSE\nRESIN\nTREND"
    assert expected == transpose(input_value)


if __name__ == "__main__":
    test_empty_string()
    test_two_characters_in_a_row()
    test_simple()
    test_square()
    print("Success")
