def stone_wall(wall):
    wall = wall.strip()
    wall_lines = wall.splitlines()

    max_value = 0
    max_index = 0
    for i in range(len(wall_lines[0])):
        current_sum = 0
        for j in wall_lines:
            if j[i] == '0':
                current_sum += 1
        if current_sum > max_value:
            max_value = current_sum
            max_index = i

    return max_index


if __name__ == '__main__':
    s = '''
##########
####0##0##
00##0###00
'''
    print(stone_wall(s))
