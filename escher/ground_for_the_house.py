def house(ground: str):
    ground = ground.strip()
    ground_list = ground.splitlines()

    min_j = len(ground_list[0])
    max_j = 0
    min_i = len(ground_list)
    max_i = 0

    for n, i in enumerate(ground_list):
        if '#' in i:
            if n < min_i:
                min_i = n
            if n > max_i:
                max_i = n
            if i.index('#') < min_j:
                min_j = i.index('#')
            if i.rindex('#') > max_j:
                max_j = i.rindex('#')

    if min_i <= max_i and min_j <= max_j:
        print((max_i-min_i+1)*(max_j-min_j+1))
    else:
        print('No house')


if __name__ == '__main__':
    s = '''
###
'''
    house(s)
