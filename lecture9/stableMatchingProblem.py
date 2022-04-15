### Stable Matching Problem ###

men = {0: [0, 2, 1],
       1: [1, 0, 2],
       2: [1, 2, 0]}
women = {0: [0, 1, 2],
         1: [2, 0, 1],
         2: [0, 1, 2]}


free_man = list(men.keys())
nr_free_man = len(free_man)

couples = [-1]*nr_free_man  #indexes indicate women, values indicate men

while nr_free_man > 0:
    m = free_man.pop(0)
    w = men[m].pop(0)
    if couples[w] == -1:
        couples[w] = m
        nr_free_man -= 1
    else:
        current_partner = couples[w]
        if women[w].index(current_partner) > women[w].index(m):
            free_man.append(current_partner)
            couples[w] = m
        else:
            free_man.append(m)
            
for i in range(len(couples)):
    print(i, couples[i])
