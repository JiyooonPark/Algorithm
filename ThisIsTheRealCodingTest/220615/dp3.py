# ==========================NOTEPAD============================
'''
2022/06/15
START: 20:15    END: 14:23

CHAPTER 8: DP

IDEAS:
    ::::
    - 1*2, 2*1, 2*2
    - 2*N
    - 2*2 = (1*2)*2 = (2*1)*2

    - main idea is to figure out how many 2*2 are going to go in.
    - cuz the 1*2 has to go in twos, and the leftovers can be filled with 2*1,
    - question -> are the blocks the same or different?
    - question -> does order matter? Or is the total blocks used more important

    - 2*3:
    ===
    2*3

    - 3**(n//2)*(n%2)*(n//2+1)
    - 3**1 * 1*2
NOTE:
    ::BFS::
'''

# ===================MY SOLUTION FUNCTION======================
def solution(n):
    return 3**(n//2)*(n%2)*(n//2+1)
# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================

# ============================MAIN=============================
if __name__ == "__main__":
    print(solution())