# ==========================NOTEPAD============================
'''
2022/06/10
START: 14:06    END: 14:23

CHAPTER 7: Binary Search
IDEAS:
    ::DFS::

NOTE:
    ::BFS::
'''

# ===================MY SOLUTION FUNCTION======================
def rec_binary_search(array, start, end, goal):
    middle_index = (start+end)//2
    if start > end:
        return False
    if array[middle_index] == goal:
        return middle_index+1
    elif array[middle_index]<goal:
        return rec_binary_search(array, start, middle_index-1, goal)
    else:
        return rec_binary_search(array, middle_index+1, end, goal)

def iter_binary_search(array, goal):
    start, end = 0, len(array)-1
    while start<end:
        middle_index = (start+end)//2
        if array[middle_index]==goal:
            return middle_index+1
        # elif start>end:
        #     return False
        elif array[middle_index]<goal:
            end = middle_index-1
        else:
            start = middle_index+1
# ======================BASIC FUNCTIONS========================

import sys
input_data = sys.stdin.readline().rstrip()

# ========================TEST CASES===========================
array = [2, 3, 14, 5, 1, 3, 52, 6, 3, 43, 4,3, 25]
array.sort()
# ============================MAIN=============================
if __name__ == "__main__":
    print(array)
    print(rec_binary_search(array, 0, len(array)-1, 44))
    print(iter_binary_search(array, 4))