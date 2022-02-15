
def subset(capacity, items):
    """
        Given a capacity and a list of positive-number items, subset returns
        the largest sum that can be made from the items without exceeding
        the capacity. 
    """
    if capacity <= 0 or items == [ ]:
        return 0
    elif items[0] > capacity:                              
        return subset(capacity, items[1:])
    else:
        useIt = items[0] + subset(capacity - items[0], items[1:])
        loseIt = subset(capacity, items[1:])
        return max(useIt, loseIt)


def knapsack(capacity, items):
    if capacity <= 0 or items == []:
        return 0
    elif items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        useIt = items[0][1]+ knapsack(capacity - items[0][0], items[1:])
        loseIt = knapsack(capacity, items[1:])
        return max(useIt, loseIt)

print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))

def change(amount, coins):
    if amount <= 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount,coins[1:])
    else:
        useIt = 1 + change(amount - coins[0], coins)
        loseIt = change(amount, coins[1:])
        return min(useIt, loseIt)


  