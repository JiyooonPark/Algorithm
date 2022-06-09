# ==========================NOTEPAD============================
'''
'''

# ===================MY SOLUTION FUNCTION======================
def bucket_sort(array):
    bucket = {}
    sorted_array = []
    for i in range(10):
        bucket[i]=0
    for i in array:
        bucket[i]+=1

    for i in bucket.keys():
        sorted_array += [i]*bucket[i]
    return sorted_array
# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================
array = [2, 3, 4, 1, 2, 6, 4, 5, 7, 9, 0, 3, 4, 1, 2, 5]
# ============================MAIN=============================
if __name__ == "__main__":
    print(bucket_sort(array))