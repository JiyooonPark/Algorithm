a = [1, [2, 2], 3]
# b = [3, 4, 5]
# print(a+b)
# a.append(4)
# print(a)
# for i in range(3):
#     a.append(i*8)
#     print(a)
# c = [[2, 3], [4, 5]]
# print(set(c))
print([2, 2] in a)

# https://www.acmicpc.net/problem/15684
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# n = int(input())
# final = list(map(int, input().split()))
final = [3, 2, 1, 4]

candidates =[[1, 2, 3, 4]]
candidates_waitlist = []
for c in candidates:
    print("======c=====", c, len(candidates))
    for i in range(2): # 0, 1, 2, 3
        print("i ::::::::::::::", i)
        temp = c[:]
        temp[i], temp[i+1] = temp[i+1], temp[i]
        print("+++++temp++++++++",temp, candidates_waitlist)
        if temp not in candidates:
            candidates_waitlist.append(temp[:])
            # print("appending:", temp, "now", candidates_waitlist)
            print(candidates, temp)
        # print(candidates)
        # else:
        #     continue
        if temp == final:
            break
        else:
            continue
# candidates_waitlist = set(candidates_waitlist)
candidates.extend(candidates_waitlist)



