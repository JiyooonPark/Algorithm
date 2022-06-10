# ==========================NOTEPAD============================
'''
2022/06/10
START: 14:30    END: 14:39

CHAPTER 7: Binary Search
IDEAS:
    ::inner sort, binary search::
    - inner sort to sort list
    - go through all requested items and binary search => logN*M
    - go through all items and see if it is there => N

NOTE:
    - could use three different methods to solve it.
'''
# ===================MY SOLUTION FUNCTION======================
def solution(storage, request):
    storage.sort()
    answer =''
    for i in request:
        start, end = 0, len(storage) - 1
        while start<=end:
            mid = (start+end)//2
            if storage[mid] == i:
                answer += "Yes "
                break
            elif storage[mid]<i:
                start = mid+1
            else:
                end = mid-1
        if start>end:
            answer+="No "
    return answer

def solution1(storage, requests):
    answer = ''
    for i in requests:
        if i in storage:
            answer+='Yes '
        else:
            answer+='No '
    return answer

def solution2(storage, requests):
    box = [0]*100001
    answer = ''
    for i in storage:
        box[i] = 1

    for i in requests:
        if box[i] == 1:
            answer += 'Yes '
        else:
            answer += 'No '
    return answer
# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================
storage = [8, 3, 7, 9, 2]
request = [5, 7, 9]
# ============================MAIN=============================
if __name__ == "__main__":
    print(solution(storage,request))
    print(solution1(storage,request))
    print(solution2(storage,request))