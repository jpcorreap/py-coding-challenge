Coding Challenge 1 Test Suite

require 'minitest/autorun'
require_relative 'book_store'

class BookStoreTest < Minitest::Test
  def test_only_a_single_book
    # skip
    basket = [1]
    assert_equal 8.00, BookStore.calculate_price(basket)
  end

  def test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three
    skip
    basket = [1, 1, 2, 3, 4, 4, 5, 5]
    assert_equal 51.20, BookStore.calculate_price(basket)
  end

  def test_two_each_of_first_4_books_and_1_copy_each_of_rest
    skip
    basket = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    assert_equal 55.60, BookStore.calculate_price(basket)
  end

  def test_two_copies_of_each_book
    skip
    basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert_equal 60.00, BookStore.calculate_price(basket)
  end

  def test_three_copies_of_first_book_and_2_each_of_remaining
    skip
    basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
    assert_equal 68.00, BookStore.calculate_price(basket)
  end

end
