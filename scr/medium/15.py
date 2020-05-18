import numpy as np
import itertools
import copy
def threeSum(nums):
    result = []
    me = list(itertools.combinations(nums,3))
    me =list(map(list, set(map(tuple, me))))
    for i in range(len(me)):
        me[i] = sorted(list(me[i]))
    me = list(map(list, set(map(tuple, me))))
    for j in range(len(me)):
        if sum(me[j])==0:
            result.append(list(me[j]))
    return result




print(threeSum( [-1, 0, 1, 2, -1, -4]))
