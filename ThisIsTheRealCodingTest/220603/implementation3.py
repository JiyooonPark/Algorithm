
'''
find the x, y coordinates of the init_pose
    use ord, chr to get the relative positions
    in the 4th plane xy coordinate
go through for loop to get all the possible positions
in for loop, check if it is within the boundary
    if it surpasses the 4th plane then not valid
'''

def solution1(init_pose):

    move = [[-2,1], [-2, -1], [2, -1], [2, 1], [-1, 2], [-1, -2], [1, -2], [1, 2]]
    possible = []
    x, y = ord(init_pose[0])-ord('a'), ord(init_pose[1])-ord('1')
    print(f'INIT POSE: ({x}, {y})')
    for mx, my in move:
        new_pose = [x+mx, y+my]
        print(f'new pose: {new_pose}')
        if 0<=new_pose[0]<=7 and 0<=new_pose[1]<=7:
            possible.append(new_pose)
    print('POSSIBLE: #', len(new_pose))
    for i in possible:
        p_pose = chr(i[0]+ord('a'))+str(i[1]+1)
        print(p_pose)

solution1('a1')
