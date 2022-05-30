
def solution1(n, k):
    step = 0

    while n!=1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        step+=1
        # print(n)
    print(step)

def solution2(n, k):
    step = 0

    while n!=1:
        if n % k == 0:
            n /= k
            step += 1

        else:
            sub = n%k
            n -= sub
            step += sub
        # print(n)
    print(step)

solution2(25,5)
solution2(17, 4)