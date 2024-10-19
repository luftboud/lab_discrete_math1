'''
Functions for reading relations from file which contains matrix 
and writing new file according to given relations
'''

# # ****************************************
# # Task 1
# # ****************************************

def matrix_to_relations(matrix):
    '''
    A function for turning matrix into a list of relations.
    :param matrix: list, a list of lists which contain number of 0 and 1 and represents a matrix.
    :return: list, a list of tuples, each of which contain two digits - (x,y є Z)(x >= 1, y >= 1) - 
    and represents relations.
    '''
    a = 0
    b = -1
    lst = []
    size = len(matrix)
    while a < size:
        b += 1
        if matrix[a][b] == '"1"':
            lst.append((a + 1, b + 1))
        if b == 4:
            b = -1
            a += 1
    return lst


def relations_to_matrix(arr, size):
    '''
    Function for turning list of relations into a matrix.
    :param arr: list, a list of matrix relations.
    :param size: int, the size of matrix
    :return: list, a list of lists which contain number of 0 and 1 and represents a matrix.
    '''
    matrix = [['"0"' for _ in range(size)] for _ in range(size)]
    for relation in arr:
        x, y = relation[0]-1, relation[1]-1
        matrix[x][y] = '"1"'
    csv = '\n'.join([','.join(map(str, row)) for row in matrix])
    return csv


def read_file(file_name):
    '''
    A function which reads filea for turning it into a list of relatives.
    :param file_name: str, a path to the file which should be read.
    :return: list, a list of tuples with matrix turned into relatives.
    >>> read_file("lab_discrete_math1/test_csv.csv")
    [(1, 3), (1, 5), (2, 1), (2, 4), (2, 5), (3, 1), (3, 3), (3, 5),\
 (4, 2), (4, 4), (5, 1), (5, 2), (5, 5)]
    '''
    with open(file_name, "r") as file:
        content = file.read()
        lines = content.splitlines()
        matrix = [line.split(',') for line in lines]
        return matrix_to_relations(matrix)


def write_file(new_file_name, relations, size):
    '''
    Function for creating a new file with relations turned into matrix.
    :param new_file_name: str, name with which a new file will be called
    :param relations: list, a list of tuples, each of which contain two digits,
    representing relations.
    :param size: int, the size of matrix
    :return: None, function generates new file with matrix in it.
    >>> relations =[(1,1), (2,2), (3,3), (4,4), (5,5)]
    >>> write_file("matrix1", relations, 5)
    '''
    with open(f"lab_discrete_math1/{new_file_name}.csv", "w") as file:
        file.write(relations_to_matrix(relations, size))


# # ****************************************
# # Task 2
# # ****************************************




if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
