'''
Functions for reading relations from file which contains matrix 
and writing new file according to given relations
'''


def matrix_to_relations(matrix):
    '''
    A function for turning matrix into a list of relations.
    :param matrix: list, a list of lists which contain number of 0 and 1 and represents a matrix.
    :return: list, a list of tuples, each of which contain two digits - (x,y є N) - 
    and represents relations.
    '''
    a = 0
    b = -1
    lst = []
    size = len(matrix)
    while a < size:
        b += 1
        if matrix[a][b] == "1":
            lst.append((a + 1, b + 1))
        if b == size-1:
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
    csv, new_line = '', '\n'
    matrix = [[ "0" for _ in range(size)] for _ in range(size)]
    for relation in arr:
        x, y = relation[0]-1, relation[1]-1
        matrix[x][y] = "1"
    for i, row in enumerate(matrix):
        row = [str(el) for el in row]
        line = ''.join(row)
        if i == len(matrix) - 1:
            new_line = ''
        csv += line + new_line
    return csv


# # ****************************************
# # Task 1
# # ****************************************

def read_file(file_name):
    '''
    A function which reads filea for turning it into a list of relatives.
    :param file_name: str, a path to the file which should be read.
    :return: list, a list of tuples with matrix turned into relatives.
    >>> read_file("lab_discrete_math1/matrix1.csv")
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    '''
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        lines = content.splitlines()
        matrix = []
        for row in lines:
            matrix.append(row)
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
    with open(f"lab_discrete_math1/{new_file_name}.csv", "w", encoding="utf-8") as file:
        file.write(relations_to_matrix(relations, size))


# # ****************************************
# # Task 2
# # ****************************************


def find_reflexive_closing(relations, file_name, size):
    """
    Function for matrix reflexive closing. It gets a list of relations, makes it reflexive,
    and creates a new file.
    :param relations: list, a list of tuples, each of which contain two digits - 
    (x,y є N) - and represents relations.
    :param file_name: str, name with which a new file will be called + prefix "reflexive_".
    :param size: int, the size of matrix.
    >>> find_reflexive_closing([(1,2), (1,3), (2,3), (3,1)], "matrix123", 3)
    """
    for el in range(1, size+1):
        if not (el,el) in relations:
            relations.append((el,el))
    write_file(f"reflexive_{file_name}", sorted(relations), size)


def find_symmetrical_closing(relations, file_name, size):
    """
    Function for matrix symmetrical closing. It gets a list of relations, makes it symmetrical,
    and creates a new file.
    :param relations: list, a list of tuples, each of which contain two digits - 
    (x,y є N) - and represents relations.
    :param file_name: str, name with which a new file will be called + prefix "symmetrical_".
    :param size: int, the size of matrix.
    >>> find_symmetrical_closing([(1,2), (1,3), (2,3), (3,1)], "matrix123", 3)
    """
    for el in relations:
        x1, x2 = el[1], el[0]
        if not (x1,x2) in relations:
            relations.append((x1,x2))
    write_file(f"symmetrical_{file_name}", sorted(relations), size)


# # ****************************************
# # Task 3
# # ****************************************


def find_transitive_closing(relations, file_name, size):
    """
    Function for matrix transitive closing. It gets a list of relations, converts it into
    binary matrix, uses Warshall algorithm so it becomes transitive and (re)writes a file.  
    :param relations: list, a list of tuples, each of which contain two digits - 
    (x,y є N) - and represents relations.
    :param file_name: str, name with which a new file will be called + prefix "transitive_".
    :param size: int, the size of matrix.
    >>> relations =[(1,1), (1,2), (2,2), (2,3), (3,3), (3,4), (4,4), (5,5)]
    >>> find_transitive_closing(relations, "matrix55", 5)
    """
    new_matrix = []
    matrix = relations_to_matrix(relations, size)
    matrix = [[int(num) for num in el] for el in matrix.split("\n")]
    w_matrix = matrix
    for i, i_row in enumerate(matrix):
        for j, j_row in enumerate(matrix):
            if i == j:
                w_matrix[j] = i_row
            if j_row[i] == 1:
                for k, _ in enumerate(j_row):
                    j_row[k] = j_row[k] or i_row[k]
            w_matrix[j] = j_row
    for i, row in enumerate(w_matrix):
        row = [str(el) for el in row]
        line = ''.join(row)
        new_matrix.append(line)
    new_matrix = matrix_to_relations(new_matrix)
    write_file(f"transitive_{file_name}", new_matrix, size)


# # ****************************************
# # Task 4
# # ****************************************


def find_equivalence_classes(relations, size):
    """
    Find equivalence classes based on relations which represent matrix.
    :param relations: list, a list of tuples, each of which contain two digits - 
    (x,y є N) - and represents relations.
    :param size: int, the size of matrix.
    >>> relations = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,4)]
    >>> find_equivalence_classes(relations, 4)
    [[0, 1, 2], [3]]
    """
    matrix = relations_to_matrix(relations, size)
    matrix = matrix.split("\n")
    classes = []
    for el in matrix:
        nums = []
        for i, n in enumerate(el):
            if n == "1":
                nums.append(i)
        if nums not in classes:
            classes.append(nums)
    return classes


# # ****************************************
# # Task 5
# # ****************************************



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
