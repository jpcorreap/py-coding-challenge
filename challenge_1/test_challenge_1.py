# Coding Challenge #1 Test Suite
from challenge_1 import calculate_price


def test_only_a_single_book():
    basket = [1]
    expected = 8.00
    assert expected == calculate_price(basket)


def test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three():
    basket = [1, 1, 2, 3, 4, 4, 5, 5]
    expected = 51.20
    assert expected == calculate_price(basket)


def test_two_each_of_first_4_books_and_1_copy_each_of_rest():
    basket = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    expected = 55.60
    assert expected == calculate_price(basket)


def test_two_copies_of_each_book():
    basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    expected = 60.00
    assert expected == calculate_price(basket)


def test_three_copies_of_first_book_and_2_each_of_remaining():
    basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
    expected = 68.00
    assert expected == calculate_price(basket)


if __name__ == "__main__":
    test_only_a_single_book()
    test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three()
    test_two_each_of_first_4_books_and_1_copy_each_of_rest()
    test_two_copies_of_each_book()
    test_three_copies_of_first_book_and_2_each_of_remaining()
    print("Success")
