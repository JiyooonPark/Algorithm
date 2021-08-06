def solution_try1(m, n, deck):
    for list in deck:
        list.sort()
        print(list)
    max = deck[0][0]
    for list in deck:
        temp = list[0]
        if temp > max:
            max = temp
        else:
            continue
    return max

def solution_better(m, n, deck):
    result = 0
    for i in range(len(deck)):
        min_val = min(deck[i])
        result = max(result, min_val)
        # print( result)
    return result
def generate_inputs(max_n, max_m):
    import random
    deck = []
    temp = []
    max_m = random.randint(1, max_m)
    max_n = random.randint(1, max_n)

    for i in range(1, max_m):
        for j in range(1, max_n):
            temp.append(random.randint(1, 100))
        deck.append(temp)
        temp = []
    return max_m, max_n, deck
if __name__ == '__main__':
    list = []
    max_n = 20
    max_m = 20
    m, n, deck = generate_inputs(max_n, max_m)
    # print(deck)
    print(solution_try1(m, n, deck))
    print(solution_better(m, n, deck))