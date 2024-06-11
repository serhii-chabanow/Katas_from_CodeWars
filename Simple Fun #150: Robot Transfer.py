def robot_transfer(matrix, k):
    n = len(matrix)
    count = 0

    def parse_coordinates(coord):
        x, y = map(int, coord.split(','))
        return x, y

    for i in range(n):
        for j in range(n):
            x, y = i, j
            for _ in range(k):
                x, y = parse_coordinates(matrix[x][y])
            if x == i and y == j:
                count += 1
    return count
