# -*- coding: utf-8 -*-
COSTS_WITH_DISCOUNTS = [8, 15.2, 21.6, 25.6, 30]
DIFFERENT_BOOKS = 5


def get_initial_matrix(basket):
    # Counts ammount of each book type.
    books_count = [0] * DIFFERENT_BOOKS

    # Counts max repetitions of same book.
    # This will define the length of aux matrix used to check groups.
    max_repeated_book = 0

    # O(N) complexity
    for book in basket:
        # Counts the book.
        books_count[book - 1] += 1

        # Look if this type of book has more repetitions than the others.
        if books_count[book - 1] > max_repeated_book:
            max_repeated_book = books_count[book - 1]

    # O(5) = O(1) complexity
    return (
        [[1]*books_count[i] + [0]*(max_repeated_book - books_count[i]) for i in range(5)],
        max_repeated_book
    )


def calculate_price(basket: list) -> float:
    # Final cost of the basket
    cost = 0

    # Books will be between 0 and 4 instead of 1 to 5 just for simplicity.
    # O(N) complexity
    matrix, max_repeated_book = get_initial_matrix(basket)

    # Counts distinct books groups than can be arranged.
    groups_count = [0] * DIFFERENT_BOOKS

    # O(N) complexity, because in worst all books are the same, max_repeated_book = n
    for j in range(max_repeated_book):
        distinct_books = 0

        for i in range(DIFFERENT_BOOKS):
            distinct_books += matrix[i][j]

        groups_count[distinct_books - 1] += 1
        # Unique worth exchange is replacing 5-3 groups for 2 groups of 4.
        # I recognize this should not been hardcoded like that, but...
        # work smarter, not harder (?)
        if groups_count[2] > 0 and groups_count[4] > 0:
            groups_count[2] -= 1
            groups_count[4] -= 1
            groups_count[3] += 2

    # O(5) = O(1) complexity.
    for i in range(DIFFERENT_BOOKS):
        cost += COSTS_WITH_DISCOUNTS[i] * groups_count[i]

    return cost
