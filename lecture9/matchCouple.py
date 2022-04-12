
men = {
    0: [0, 1, 2],
    1: [0, 2, 1],
    2: [1, 0, 2]
}
women = {
    0: [1, 2, 0],
    1: [1, 0, 2],
    2: [2, 0, 1]
}

free_man = list(men.keys())
num_free_man = len(free_man)

couples = [-1] * num_free_man  # index represent woman, value represent man


while num_free_man > 0:
    m = free_man.pop(0)
    w = men[m].pop(0)
    if (couples[w] == -1):
        couples[w] = m
        num_free_man -= 1
    else:
        current_partner = couples[w]
        if (women[w].index(current_partner) > women[w].index(m)):
            free_man.append(current_partner)
            couples[w] = m
        else:
            free_man.append(m)

for i in range(len(couples)):
    print(i, couples[i])
