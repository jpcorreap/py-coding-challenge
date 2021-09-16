# -*- coding: utf-8 -*-

# Calculates all possible discount groups
BOOK_PRICE = 8
DISCOUNTS = [0.05, 0.1, 0.2, 0.25]
DIFFERENT_BOOK_TYPES = 5

# This dictionary contains final prices of a group of different books,
# for example, a set of 2 different books costs 15.2, a set of 3 costs 30
final_costs_with_discount = {i: BOOK_PRICE*i*(1-DISCOUNTS[i-2])
                             for i in range(2, DIFFERENT_BOOK_TYPES + 1)}
final_costs_with_discount[1] = BOOK_PRICE


def combinate(lst, n):
    if n == 0:
        return [[]]
    l =[]
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1:]
        for p in combinate(remLst, n-1):
            l.append([m]+p)
    return l


def are_compatible_groups( group1, group2, histogram ):
    are_compatible = True

    for i in group1:
        if histogram[i] > 0:
            histogram[i] -= 1
        else:
            are_compatible = False

    for j in group2:
        if histogram[j] > 0:
            histogram[j] -= 1
        else:
            are_compatible = False

    return are_compatible


def get_viable_combinations(combinations, histogram):
    if len(combinations) == 0:
        return []

    left = combinations[0]
    right = combinations[1:]

    viable_combination = []
    #for combination in combinations:
    #    print(combinations)

def calculate_price(basket: list) -> int:
    combinations = [[basket[i:j] for i in range(len(basket) + 1) for j in range(i + 1, len(basket) + 1)]]
    
    recombinations = [[combinations[x:y] for x in range(len(combinations) + 1) for y in range(x + 1, len(combinations) + 1)]]
    # Count ammount of books of each type
    histogram = { x : 0 for x in set(basket)}
    for i in basket:
        histogram[i] += 1

    print(recombinations)
    #print(histogram)
    
    #all_possible_distinct_groups = []
    #for scenario in combinations:
    #    for group in scenario:
    #        uniques = list(set(group))
    #        if len(group) > 0:
    #            all_possible_distinct_groups.append(uniques)
                
    #print(all_possible_distinct_groups)
    return 0


calculate_price([1, 2])
#calculate_price([1, 2])
