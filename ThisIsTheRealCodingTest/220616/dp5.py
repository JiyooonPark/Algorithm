# ==========================NOTEPAD============================
'''
2022/06/16
START: 20:55    END: 21:10

CHAPTER 8: DP

IDEAS:
    ::DP->memoize->big to small ::
    - 2: 2
    - 3: 3
    - 4: 2/2
    - 5: 2/3
    - 6: 3/3
    - 7: 2/2/3

    recursive -> -3, -2 -> min
    if in array-> return
    else: rec
    - min(poss)

NOTE:
    - used memoize + bottom up
    - which is faster? => the book's way is faster
    - why dp we have to put d[0] = 0? how do I know to put this here?

    ==> if I use recursion, it exceeds the stack limit easily.
    - better to use the bottom up way using the for- loop
'''

# ===================MY SOLUTION FUNCTION======================
d = dict()
INF = 10000000000

def solution(m, k):
    poss = []
    if m<min(k):
        return INF
    if m not in d.keys():
        for i in k:
            if m-i >0:
                poss.append(solution(m-i, k))
        d[m]= min(poss)+1
    return d[m] if d[m] <=INF else -1

def book_solution(m, k):
    n = len(k)
    d = [INF]*(m+1)
    d[0] = 0
    for i in k:
        for j in range(i-1, m+1):
            if d[j-i] != INF:
                d[j] = min(d[j], d[j-i]+1)
    return d[j] if d[j] != INF else -1
# ======================BASIC FUNCTIONS========================
import time
def start_time():
    return time.time()
def total_time(st):
    return time.time()-st
# ========================TEST CASES===========================
N = 2
M = 2318
K = [2, 3, 4, 7]
# M, K = 4, [3, 5, 7]
for i in K:
    d[i] = 1
print(d)
# ============================MAIN=============================
if __name__ == "__main__":
    st = start_time()
    # print(solution(M, K))
    print(total_time(st))
    st = start_time()
    print(book_solution(M, K))
    print(total_time(st))