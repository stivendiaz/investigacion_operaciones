import numpy as np

np.set_printoptions(precision=3)

def disparity_index(m1, m2):
    shared_pieces = len(m1.intersection(m2))
    processed_pieces = len(m1.symmetric_difference(m2))
    return 1 - shared_pieces / (shared_pieces + processed_pieces)

def main(machines):
    assert len(machines) > 1, 'You need at least two machines.'
    matrix = list(np.zeros((len(machines), len(machines))))
    for i, machine in enumerate(machines):
        last_index = i
        for j, machine2 in enumerate(machines[i+1:]):
            disparity = disparity_index(machine, machine2)
            matrix[i][last_index+1] = disparity
            matrix[last_index+1][i] = disparity
            last_index += 1
    return matrix

if __name__ == '__main__':
    A = main([
        {1, 6},
        {2, 3, 7, 8, 9, 12, 13, 15},
        {3, 5, 10, 14},
        {2, 7, 8, 11, 12, 13},
        {3, 5, 10, 11, 14},
        {1, 4, 5, 9, 10},
        {2, 5, 7, 8, 9, 10},
        {3, 4, 15},
        {4, 10},
        {3, 8, 10, 14, 15},
    ])
    print(np.array(A))
