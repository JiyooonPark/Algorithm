# my solution
def solution_my(B, pose):
    possible = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    count =0
    for p in possible:
        if 0<pose[0] + p[0] <8 and 0<pose[1]+ p[1]<8:
            count +=1
        else:
            continue
    return count

# given solution
def solution_given():
    #same
    pass
def generate_inputs():
    B = []
    temp = []
    for i in range(1, 9):
        for j in range(1, 9):
            temp.append(j)
        B.append(temp)
        temp = []
    import random
    pose = [random.randint(1, 8), random.randint(1, 8)]
    return B, pose
if __name__ == '__main__':
    max_n = 1000
    B, pose = generate_inputs()

    print(pose)
    # pose=[3,2]
    print(solution_my(B, pose))