# ==========================NOTEPAD============================
'''
2022/06/13
START: 14:08    END: 14:23

CHAPTER 8: Dynamic Programming

IDEAS:
    ::DFS::

NOTE:
    - call (n-1) before (n-2) in fib
'''

# ===================MY SOLUTION FUNCTION======================
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
d = [0]*100

def fib_dynamic(n):

    if n<=2:
        return 1
    if d[n] == 0:
        d[n] = fib_dynamic(n-1)+fib_dynamic(n-2)
    return d[n]

# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================

# ============================MAIN=============================
if __name__ == "__main__":
    print(fib(10))
    print(fib_dynamic(10))