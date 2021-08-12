
def solution(user_input):
    # 총 점수를 저장하기 위한 변수
    total_score = 0
    # 'O'이 지속되는 횟수를 저장하기 위한 변수
    score = 0

    # 매 문제마다 점수를 업데이트한다
    for a in list(user_input):
        if a == "O":
            # 'O'가 지속될 경우 누적해서 score을 더한다
            score += 1
        else:
            # 'X'를 만나면 점수를 다시 0으로 초기화시킨다
            score = 0
        # 매 문제마다 총점수를 업데이트 한다
        total_score += score

    return total_score


if __name__=='__main__':
    user_input = input()
    if len(user_input) > 1000:
        print('입력 범위를 초과하였습니다.\n')
        exit(1)
    print(solution(user_input))


# user_input = "OOXXOXXOOOO"
# user_input = "OOXXOXXOOOXOXOXO"