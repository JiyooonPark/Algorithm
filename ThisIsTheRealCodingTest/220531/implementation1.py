
def solution1(n, n_list):
    dir={'U':(-1,0), 'D':(1,0), 'R':(0,1), 'L':(-1,0)}
    pose = [1,1]
    for letter in n_list:
        next = [pose[0]+dir[letter][0],pose[1]+dir[letter][1]]
        if 0<next[0]<=n and 0<next[1]<=n:
            pose = next
        else:
            continue
    print(pose)

solution1(5, ['R','R','R','U','D','D'])

