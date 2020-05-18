import numpy as np
def longestCommonPrefix(strs):
    if len(strs)==0:
        return ""
    num = ""
    flag = True
    max_len = min(strs)
    for i in range(len(max_len)):
        for j in range(1,len(strs)):
            if strs[0][i]!=strs[j][i]:
                flag = False
                break
        if flag:
            num+=strs[0][i]
        else:
            break
    return num




print(longestCommonPrefix(["flower","flow","flight"]))
