# ==========================NOTEPAD============================
'''
2022/06/15
START: 18:40    END: 20:00

CHAPTER 6: DP

IDEAS:
    ::DP recursion::
    - nothing -> the dumb way
        - go through all the possibilities
        - select/don't select -> 2^n

    -recursion
        - sol(n)
            - if
    - memoize
        - storage
        - sol(n)
            - ffj;dsjhjkdfsjkdfskjhjkdfsjksdfjsdjk

    - go from the back -> if start is here, then this is the max
    - when reach first element, then stop?
    sol(p):
    if p==0:
        return max?
    workspace = n[p:]
====================================================================================
    poss = []
    if len(p) == 1:
        return P

    for i in list:
        poss.append( sol([:i-1])+i + sol([i+2:]))
    return max(poss)

NOTE:
    ::DP bottom up + memoize::
    - from the front, store max selection
    - work its way to the end and decide which to take.

    = Cut the problem to relevant/irrelevant parts

'''

# ===================MY SOLUTION FUNCTION======================
def solution(k):
    poss = []
    if len(k)==0:
        return 0
    elif len(k) == 1:
        return k[0]
    elif len(k) == 2:
        return max(k)
    else:
        # print(len(k))
        for i in range(1, len(k)-1):  # 1, 2, 3
            p = solution(k[:i-1])+k[i]+solution(k[i+2:])
            poss.append(p)
            # print(f"i: {i} P: {p}")
        return max(poss)

def solution_answer(k):
    arr = [-1]*len(k)
    arr[0] = k[0]
    arr[1] = max(k[:2])

    for i in range(2, len(k)):
        arr[i] = max(arr[i-1], arr[i-2]+k[i])
    return arr[len(k)-1]
# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================
N = 4
K = [1, 3, 1, 5]
K1 = [1, 1, 3, 5]
K1 = [1, 8, 1, 9, 9, 1, 1, 9] # 8, 9, 1, 9 = 18+9 = 27
# ============================MAIN=============================
if __name__ == "__main__":
    print(solution(K1))
    print(solution_answer(K1))