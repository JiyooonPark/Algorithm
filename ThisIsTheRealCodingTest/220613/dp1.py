# ==========================NOTEPAD============================
'''
2022/06/13
START: 15:45    END: 14:23

CHAPTER 8: Dynamic Programming

IDEAS:
    ::::
    - think bottom->up
    - from 1 what is the fastest way to get to n?
    - for all numbers, fastest way to get there -> store in dict

NOTE:
    - I was partially right, but the implementation was completely out of the blue
    - took me a while to understand why the answer code is as is.
'''

# ===================MY SOLUTION FUNCTION======================
d={1:0}

def solution(n):

    for i in range(2, n+1):
        poss = [d[i-1]+1]
        if i%2 == 0:
            poss.append(d[i/2]+1)
        elif i%3 == 0:
            poss.append(d[i/3]+1)
        elif i%5 == 0:
            poss.append(d[i/5]+1)
        d[i] = min(poss)
        print(d)

# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================

# ============================MAIN=============================
if __name__ == "__main__":
    solution(26)