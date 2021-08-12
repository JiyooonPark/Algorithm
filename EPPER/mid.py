# https://alpyrithm.tistory.com/134
def solution(cities, distance, price):
    # 총 주유 가격
    cost = 0
    # 처음 시작할때에는 다음 도시로 가기 위해 무조건 주유를 해야한다
    min_cost = price[0]
    # 모든 도시를 다 방문하는동안,
    for i in range(cities - 1):
        # 최소비용의 도시를 찾고 ( 지나온 도시 + 현 도시)
        if price[i] < min_cost:
            # 만일 현 도시의 주유값이 더 쌀 경우, 최소 주유비용을 업데이트한다
            min_cost = price[i]
        # 다음도시로 가기  위한 거리와 가장 싼 주유값을 곱하여 다음 도시로 진행한다
        cost += min_cost * distance[i]
    return cost

if __name__=='__main__':
    cities = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))
    print(solution(cities, distance, price))