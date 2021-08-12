# https://www.acmicpc.net/problem/15684
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# n = int(input())
# final = list(map(int, input().split()))
import math


def solution():
    n = 10
    final = [3, 4, 5, 1, 2, 6, 7, 8, 10, 9]
    # n = 4
    # final = [2, 1, 4, 3]

    candidates =[[i for i in range(1, n+1)]]
    candidates_waitlist = []
    level = 0
    if final == candidates[0]:
        return level
    while len(candidates)!= math.factorial(n):
        for k in range(n-1):
            print('level:', level)
            print("======c=====", len(candidates))
            # print(candidates)
            level += 1
            for c in candidates:

                for i in range(n-1): # 0, 1, 2, 3
                    temp = c[:]
                    temp[i], temp[i+1] = temp[i+1], temp[i]
                    # print("+++++temp++++++++", temp)
                    if temp not in candidates:
                        candidates_waitlist.append(temp[:])
                    # print("appending:", temp, "now", candidates_waitlist)
                    if temp == final:
                        # print("*****************************************\n\n\n\n\n")
                        # print(level)
                        return level
                    else:
                        continue

            candidates.extend(candidates_waitlist)



print(solution())