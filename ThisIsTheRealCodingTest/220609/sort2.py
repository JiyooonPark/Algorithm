# ==========================NOTEPAD============================
'''
sort test
- still don't know how to do insertion sort.
- others are also kinda vague. 
'''

# ===================MY SOLUTION FUNCTION======================
def insertion_sort(array): # mine
    for i in range(1, len(array)):
        if array[i]<array[i-1]:
            for j in range(i, 0, -1):
                if array[j]<array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
    return array

def insertion_sort1(array): # book
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array
def quick_sort(array):

    if len(array)<=1:
        return array
    middle_index = len(array)//2
    left_array = [i for i in array if i<array[middle_index]]
    right_array = [i for i in array if i>array[middle_index]]
    return quick_sort(left_array)+[array[middle_index]]+quick_sort(right_array)

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================
array = [3,5,6,4,8,1,7,9,2,10,0]
# ============================MAIN=============================
if __name__ == "__main__":
    print(insertion_sort(array))
    print(quick_sort(array))
    print(selection_sort(array))