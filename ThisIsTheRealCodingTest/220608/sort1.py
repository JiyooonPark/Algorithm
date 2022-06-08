# ==========================NOTEPAD============================
''' Different kind of sort functions'''
# ===================MY SOLUTION FUNCTION======================
def selection_sort(array):

    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j]<array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    print(array)

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 1, -1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    print(array)

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array)//2
    left = [i for i in array if i<array[pivot]]
    right = [i for i in array if i>array[pivot]]
    return quick_sort(left)+[array[pivot]]+quick_sort(right)

# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================
array = [9, 6, 1, 8, 2, 4, 3, 7, 5, 10, 0]
# ============================MAIN=============================
if __name__ == "__main__":
    selection_sort(array)
    insertion_sort(array)
    print(quick_sort(array))