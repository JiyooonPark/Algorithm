# ==========================NOTEPAD============================
'''
2022/06/06
START: 20:18    END: 20:25

CHAPTER 6: sort

IDEAS:
    ::sort::
    - python inner function + dictionary + key sort

NOTE:
    - not use dictionary for input
    - but how to use dictionary and key sort?
'''

# ===================MY SOLUTION FUNCTION======================
def solution(array):
    result = sorted(array, key=setting)
    print(result)
    for i in result:
        print(i[0], end=" ")
def setting(array):
    return array[1]


def solution1(dictionary):
    result = sorted(dictionary.items(), key=setting)
    print(result)
def setting1(item):
    return item[1]
# ======================BASIC FUNCTIONS========================
# dict(sorted(x.items(), key=lambda item: item[1]))

# ========================TEST CASES===========================
array =[["Abby", 90], ["Drew", 75], ["Ella", 91], ["Dave", 70], ["Tony", 100], ["Jane", 100], ["Miley", 60]]
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# ============================MAIN=============================
if __name__ == "__main__":
    # solution1(x)
    print(x.items())