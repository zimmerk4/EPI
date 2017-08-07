import random


def uniform_random(lwr_bnd, upr_bnd):
    num_outcomes = upr_bnd - lwr_bnd + 1
    while True:
        res = 0
        i = 0
        while(1 << i) < num_outcomes:
            res = (res << 1) | random.randint(0, 1)
            i += 1
        if res < num_outcomes:
            break
    return res + lwr_bnd

# Seems fair...
# lst = []
# for i in range(1000000):
#     lst.append(uniform_random(1, 6))
#
# print("1: ", lst.count(1)/len(lst),
#       "2: ", lst.count(2)/len(lst),
#       "3: ", lst.count(3)/len(lst),
#       "4: ", lst.count(4)/len(lst),
#       "5: ", lst.count(5)/len(lst),
#       "6: ", lst.count(6)/len(lst))