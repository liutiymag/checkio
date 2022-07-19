def navigation(seaside: list):
    for n, l in enumerate(seaside):
        if 'Y' in l:
            y = (n, l.index("Y"))
        if 'C' in l:
            c = (n, l.index("C"))
        if 'M' in l:
            m = (n, l.index("M"))
        if 'S' in l:
            s = (n, l.index("S"))

    max_c = max(abs(c[0] - y[0]), abs(c[1] - y[1]))
    max_m = max(abs(m[0] - y[0]), abs(m[1] - y[1]))
    max_s = max(abs(s[0] - y[0]), abs(s[1] - y[1]))
    print(max_c+max_m+max_s)


if __name__ == '__main__':

    inp_list = [['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]
    navigation(inp_list)
