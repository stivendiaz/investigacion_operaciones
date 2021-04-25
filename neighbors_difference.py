import numpy as np

def calc_neighbors(i, j, size):
    lookup = [
        (i-1, j),
        (i-1, j+1),
        (i, j+1),
        (i+1, j+1),
        (i+1, j),
        (i+1, j-1),
        (i, j-1),
        (i-1, j-1),
    ]
    neighbors = []
    for row, col in lookup:
        if row >= 0 and col >= 0 and row <= size and col <= size:
            neighbors.append((row, col))
    return neighbors

def create_sorted(size):
    matrix = []
    pos = 0
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(pos)
            pos += 1
    return matrix

def main(matrix):
    m_size = len(matrix)
    all_neighbors = []
    adjacency = list(np.zeros((m_size ** 2, m_size ** 2)))
    temp = create_sorted(m_size)
    for i in range(len(temp)):
        for j in range(len(temp)):
            for row, col in calc_neighbors(i, j, m_size - 1):
                diff = abs(matrix[i][j] - matrix[row][col])
                adjacency[temp[i][j]][temp[row][col]] = diff
    return adjacency

if __name__ == '__main__':
    out = main([
        [3, 5, 7],
        [7, 6, 1],
        [1, 4, 3],
    ])
    # out = main([
    #     [30, 50],
    #     [45, 5],
    # ])
    print(np.array(out))
