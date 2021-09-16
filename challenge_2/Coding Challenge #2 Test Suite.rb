Coding Challenge #2 Test Suite

require 'minitest/autorun'
require_relative 'transpose'

class TransposeTest < Minitest::Test
  def test_empty_string
    # skip
    input = ""

    expected = ""

    assert_equal expected, Transpose.transpose(input)
  end

  def test_two_characters_in_a_row
    skip
    input = "A1"

    expected = "A\n1"

    assert_equal expected, Transpose.transpose(input)
  end

  def test_simple
    skip
    input = "ABC\n123"

    expected = "A1\nB2\nC3"

    assert_equal expected, Transpose.transpose(input)
  end

  def test_square
    skip
    input = "HEART\nEMBER\nABUSE\nRESIN\nTREND"

    expected = "HEART\nEMBER\nABUSE\nRESIN\nTREND"

    assert_equal expected, Transpose.transpose(input)
  end
end
