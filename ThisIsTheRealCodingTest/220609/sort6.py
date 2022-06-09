# ==========================NOTEPAD============================
'''
2022/06/06
START: 21:03    END: 21:07

CHAPTER 6: sort

IDEAS:
    ::sort, swap::
    - sort list A, B
    - swap k times -> A[:k] with B[-K:]
NOTE:
    - have to check if the swap is necessary!
    - simply replacing the small and big may not return the best result
'''

# ===================MY SOLUTION FUNCTION======================
def solution(a, b, k):
    a.sort()
    b.sort()
    a[:k], b[-k:] = b[-k:],a[:k]
    return sum(a)

def solution1(a,b,k):
    a.sort()
    b.sort()
    for i in range(k):
        if a[i]<b[-i]:
            a[i], b[-i] = b[-i], a[i]
    return sum(a)
# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================
A = [1, 2, 5, 4, 3]
B = [5, 5, 6, 6, 5]


# ============================MAIN=============================
if __name__ == "__main__":
    # print(B[-2:])
    print(solution1(A, B, 3))