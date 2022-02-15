def knapsack(capacity, items):
    if capacity <= 0 or items == []:
        return 0
    elif items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        use_it = items[0][1] + knapsack(capacity - items[0][0], items[1:])
        lose_it = knapsack(capacity, items[1:])
        return max(use_it, lose_it)

def knapsack_updated(capacity, items):
    """Given a container of a given integer 'capacity', and a list of items 
       'items' where each item is of the form [weight, value], returns a list 
        containing the maximum value that can fit in the capacity followed by the list of 
        all items in 'itemList' that make up this optimal arrangement."""
    if capacity <= 0 or items == []:
        return [0, []]
    elif items[0][0] > capacity:
        return knapsack_updated(capacity, items[1:])
    else:
        resultList = knapsack_updated(capacity - items[0][0], items[1:])
        use_it = [resultList[0] + items[0][1], [items[0]] + resultList[1]]   # [items[0]] + resultList[1] is order matter 
        lose_it = knapsack_updated(capacity, items[1:])
        if use_it[0] > lose_it[0]:
            return use_it
        else:
            return lose_it
        

def test_knapsack_updated():
    assert knapsack_updated(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]) == [100, [[10, 28], [39, 47], [8, 1], [7, 24]]]
    assert knapsack_updated(6, [[1, 4], [5, 150], [4, 180]]) == [184, [[1, 4], [4, 180]]]
    assert knapsack_updated(24, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]) == [52, [[10, 28], [7, 24]]]
    assert knapsack_updated(20, []) == [0, []]
    assert knapsack_updated(0, [[1, 1000], [2, 3000], [4, 55000]]) == [0, []]


# test_knapsack_updated()
# print(knapsack_updated(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
# print(knapsack_updated(6, [[1, 4], [5, 150], [4, 180]]))
# print(knapsack_updated(24, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
# print(knapsack_updated(20, []))
# print(knapsack_updated(0, [[1, 1000], [2, 3000], [4, 55000]]))