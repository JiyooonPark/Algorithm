# ==========================NOTEPAD============================
'''
2022/06/16
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
    - this is not a math question so you should not approach it this way.
    - have to make the question into a 점화식 and then code it.
    - start in the box then work your way out

    - DP question solution 1:
        - Ai = A(i-1) + A(i-2)*2
        - A1, A2 = x, x
        - for i in range(3, n)
            a[i] = a[i-1]+2*a[i-2]

'''

# ===================MY SOLUTION FUNCTION======================
def solution(n):
    # if n%2 == 0:
    #     return 3 ** (n // 2) * (n % 2) * (n // 2 + 1)-1

    return (   3**(n//2)-1   )*(  (n//2)*(n%2)    )
# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================

# ============================MAIN=============================
if __name__ == "__main__":
    print(solution(3))