File = open(r"lab_discrete_math1/test_csv.csv", "r")

content = File.read()
lines = content.splitlines()
matrix0 = [line.split(',') for line in lines]
def reading(matrix):
    '''
    
    '''
    a = 0
    b = -1
    lst = []
    while a < 5:
        b += 1
        tesotva = matrix[a][b]
        if matrix[a][b] == '"1"':
            lst.append([a + 1, b + 1])
        if b == 4:
            b = -1
            a += 1
    return lst

print(reading(matrix0))
