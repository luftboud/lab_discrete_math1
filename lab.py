with open(r"lab_discrete_math1/test_csv.csv", "r") as File:
    content = File.read()
    lines = content.splitlines()
    matrix0 = [line.split(',') for line in lines]

lst0 = [[1, 2], [1, 5], [2, 1], [2, 4], [2, 5], [3, 1], [3, 3], [3, 5], [4, 2], [4, 4], [5, 1], [5, 2], [5, 5]]

def matrix_to_relations(matrix):
    '''
    
    '''
    a = 0
    b = -1
    lst = []
    while a < 5:
        b += 1
        if matrix[a][b] == '"1"':
            lst.append([a + 1, b + 1])
        if b == 4:
            b = -1
            a += 1
    return lst

def relations_to_matrix(list):
    matrix = [['"0"' for _ in range(5)] for _ in range(5)]
    for relation in list:
        x, y = relation[0]-1, relation[1]-1
        matrix[x][y] = '"1"'
    csv = '\n'.join([','.join(map(str, row)) for row in matrix])
    return csv

print(matrix_to_relations(matrix0))
# print(relations_to_matrix(lst0))
# print(relations_to_matrix(lst0))
with open("lab_discrete_math1/test_csv.csv", "w") as File1:
    File1.write(relations_to_matrix(lst0))
