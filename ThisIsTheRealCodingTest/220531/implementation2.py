
def solution1(n):
    no_three = [i for i in range(n+1) if str(i).find('3')<0]
    count = 60*60*(n+1)-45*45*len(no_three)
    print(count)

solution1(5)

def solution2(n):
    count = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                num = str(i)+str(j)+str(k)
                if num.find('3')>=0:
                    count+=1
    print(count)
# print('15'.find('5'))

solution2(5)