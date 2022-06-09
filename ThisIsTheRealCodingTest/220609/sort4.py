# ==========================NOTEPAD============================
'''
2022/06/09
START: 20:14    END:20:15

CHAPTER 6: SORT

IDEAS:
    ::sort::
    - use python inner function

NOTE:
    - sorted(array, reverse=True)
'''

# ===================MY SOLUTION FUNCTION======================
def solution(array):
    array.sort()
    array.reverse()
    return array

def solution2(array):
    array = sorted(array, reverse=True)
    return array
# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================

# ============================MAIN=============================
if __name__ == "__main__":
    print(solution2([15, 27, 12]))