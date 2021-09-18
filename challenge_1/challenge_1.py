# -*- coding: utf-8 -*-
from itertools import permutations


DISCOUNTS = [0, 0.8, 2.4, 6.4, 10]


def get_ocurrences(basket: list) -> dict:
    """
    Counts the repetitions of each book in the basket.

    Returns
    -------
    dict
        A dictionary with count of repetitions of each book.

    """
    # Complexity of O(1) since range is const
    histogram = {x: 0 for x in range(1, 6)}

    # Complexity of O(N)
    for i in basket:
        histogram[i] += 1

    return histogram


def get_discount(matrix: list) -> float:
    """
    Calculates the discount for a given matrix of choices
    """
    discount = 0
    group_of = 0

    for j in range(len(matrix[0])):
        for i in range(0, 5):
            group_of += matrix[i][j]
        discount += DISCOUNTS[group_of - 1]
        group_of = 0

    return discount


def calculate_price(basket: list) -> float:
    # Stores the count for each same book in the basket
    # O(N) complexity
    count_by_book = get_ocurrences(basket)

    # Number of books
    N = len(basket)

    # Max number of repetitions of same book
    # This determines the length of matrix to work with
    # O(N) complexity for extracting the values
    # And then another O(N) to find max value
    L = max(count_by_book.values())

    # Original binary matrix which represents books in the basket
    # This allows each row to be a group of distinct books
    matrix = [[1]*count_by_book[i+1] + [0]*(L-count_by_book[i+1])
              for i in range(5)]

    # A list for each book with all possible permutations per row
    # I recognize this must be implemented with a for but it will imply
    #  a 3D data structure that I do not want to deal with haha
    # About complexity... I would say this is sadly an O(N!) for each one
    permutations_b1 = list(set(permutations(matrix[0], L)))
    permutations_b2 = list(set(permutations(matrix[1], L)))
    permutations_b3 = list(set(permutations(matrix[2], L)))
    permutations_b4 = list(set(permutations(matrix[3], L)))
    permutations_b5 = list(set(permutations(matrix[4], L)))

    # Best discount user can get
    # This will be used to calculate final price for each combination
    best_discount = 0

    # This is probably the most horrible part of this algorithm
    #   ...and hopelly of my entire life as a programmer as well
    # Looks for every possible combination of rows and calculates
    #  discount of that combination. The idea is to find max discount.
    # It has a complexity of O(N!^5) since each permutation list
    #  was calculated with O(N!) and for each list it must iterate
    #  over another 4 permutaton lists...
    for first_row in permutations_b1:
        for second_row in permutations_b2:
            for third_row in permutations_b3:
                for fourth_row in permutations_b4:
                    for fifth_row in permutations_b5:
                        total_discount = get_discount(
                            [first_row,
                             second_row,
                             third_row,
                             fourth_row,
                             fifth_row]
                        )

                        if total_discount > best_discount:
                            best_discount = total_discount

    # The original price is 8*number of books
    # and then it substracts the best discount
    return (8*N) - best_discount


print(calculate_price([1]))  # 8
print(calculate_price([1, 1, 2, 3, 4, 4, 5, 5]))  # 51.2
print(calculate_price([1, 1, 2, 2, 3, 3, 4, 4, 5]))  # 55.6
print(calculate_price([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))  # 60
print(calculate_price([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]))  # 68
