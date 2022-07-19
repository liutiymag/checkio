def wild_dogs(coords: list):
    lines = {}
    for i, m in enumerate(coords):
        for j, n in enumerate(coords[i + 1::]):
            if m[0] != n[0]:
                line = ((m[1] - n[1]) / (m[0] - n[0]), m[1] - m[0] * (m[1] - n[1]) / (m[0] - n[0]))
                lenght = ((line[1] / (-1 / line[0] - line[0])) ** 2 + (
                            -1 / line[0] * line[1] / (-1 / line[0] - line[0])) ** 2) ** 0.5
            else:
                lenght = m[0]
            if lines.get(line):
                lines.update({line: [lines.get(line)[0] + 1, lenght]})
            else:
                lines.update({line: [2, lenght]})
    max_key = min([i[1] for i in lines.values() if i[0] == max([i[0] for i in lines.values()])])
    return round(max_key, 2)


if __name__ == '__main__':
    crds = [[5,50],[6,60],[1,23]]
    print(wild_dogs(crds))
