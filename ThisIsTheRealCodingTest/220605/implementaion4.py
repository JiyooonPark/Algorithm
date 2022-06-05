'''
Question is wrong 

find how many squares the player can go to
stops search when backward is water

turns left
    if not been then move forward
    else if been then continue
    else go backwards
        if backward is water then stop

'''
def print_map(map_, pose, dir):
    move = {0: (0, -1, 'n'), 1: (1, 0, 'e'), 2: (0, 1, 's'), 3: (-1, 0, 'w')}
    print("MAP ==============")
    print(f"CURR: {pose}, {move[dir][-1]}")
    for i in map_:
        print(i)
    print("==================")

def padd_map(map_):
    padding = [0 for i in range(n + 2)]
    for i in map_:
        i.insert(0, 0)
        i.append(0)
    map_.insert(0, padding)
    map_.append(padding)
    return map_

def stranded(pose, map_):
    strand = True
    for i in [[0,1], [1, 0], [-1, 0], [0, -1]]:
        if map_[pose[0]+i[0]][pose[1]+i[1]] == 1:
            strand = False
    return strand

def solution1(n, m, d, map_):

    map_ = padd_map(map_)

    move = {0:(-1, 0, 'n'), 1:(0, 1,'e'), 2:(1, 0, 's'), 3:(0, -1, 'w')}

    dir = d[-1]
    pose = [d[0], d[1]]

    print(f"INIT POSE: {pose, dir} map: {map_[pose[0]][pose[1]]}")

    loop_count = 0

    while not stranded(pose, map_):
        # print(f"LOOP #{loop_count}")
        loop_count +=1

        map_[pose[0]][pose[1]] = 2
        print_map(map_, pose, dir)

        dir = (dir-1)%4
        # print(dir)

        next = [pose[0]+move[dir][0],pose[1]+move[dir][1]]
        print(f"NEXT POSE: {next}, MAP: {map_[next[0]][next[1]]}")

        if map_[next[0]][next[1]] == 1:
            pose = next
            map_[next[0]][next[1]] = 2
        elif map_[next[0]][next[1]] == 2:
            print("++ been here ")
        elif map_[next[0]][next[1]] == 0:
            print("++ is sea ")
        else:
            next = [pose[0]-move[dir][0], pose[1]-move[dir][1]]
            pose = next
            if map_[next[0]][next[1]] == 0:
                break
    count = 0
    for i in map_:
        for j in i:
            if j==2:
                count +=1

    print(count)

    pass

n = 4
m = 4
d = [1, 1, 0]
map_ = [[1,1,1,1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
print(map_[1][1])
solution1(n, m, d, map_)

# print((-1%4))