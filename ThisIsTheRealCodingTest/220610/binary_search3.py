# ==========================NOTEPAD============================
'''
2022/06/10
START: 14:46    END: 15:14

CHAPTER 7: Binary Search
IDEAS:
    ::table, for loop for rows::
    19, 15, 10, 17
    10, 15, 17, 19
    0 , 5 , 7 , 9

        17
    15      19
10

    25 15 42 52 61 =>
    61-6 = 55/4 = 14.x

    - sort the array
    - calculate the distances -> put in array
    - make calculating function
    - find max in range

    3:06


NOTE:
'''
# ===================MY SOLUTION FUNCTION======================
def solution(n, m, length):
    s = (sum(length)-m)//n

    remainder = 0
    count = 0

    while remainder>m:
        remainder = 0
        for i in length:
            if (i-s)>0:
                remainder+=(i-s)
        s += 1
        count+=1
        print(count, remainder)
    print(f"count: {count}, s: {s}")

def solution1(n, m, array):
    array.sort()
    print(array)
    distance = [0]
    for i in range(1, len(array)):
        distance.append(array[i]-array[i-1])
    print("distance:", distance)

    remainder = 0

    for i in range(len(array)):
        remainder += distance[-i]*i
        if remainder >= m:
            break
    max_len = array[-i-1]
    print("1:",max_len)



    while remainder>=m:
        max_len+=1
        remainder=0
        for i in array:
            if i-max_len>0:
                remainder+=(i-max_len)
        print(f"remainder: {remainder}, max_len: {max_len}")
        if remainder == m:
            return max_len
    max_len-=1
    return max_len

def solution2(n, m, array):
    array.sort()
    start, end = 0,array[-1]
    remainder = 0
    result =0

    while start<=end:

        remainder = 0
        mid = (start+end)//2

        for i in array:
            if i-mid>0:
                remainder += (i-mid)

        print(f"mid: {mid}, remainder: {remainder}, start: {start}, end: {end}")
        if remainder > m:
            result = mid
            start = mid+1
        else:
            end = mid-1
    print(result)



# ======================BASIC FUNCTIONS========================

# ========================TEST CASES===========================
N, M = 4, 6
array = [19, 15, 10, 17]
# 15
N, M = 4, 10
array = [19, 15, 10, 17, 13, 20]

#16
# N, M = 4, 50
# array = [19, 15, 10, 17, 13, 20, 40]
# 12
# ============================MAIN=============================
if __name__ == "__main__":

    print(solution1(N, M, array))
    print(solution2(N, M, array))
