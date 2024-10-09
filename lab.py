File = open(r"test_csv.csv", "r")

content = File.read()
lines = content.splitlines()
matrix = [line.split(',') for line in lines]

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

print(matrix)

print(lst)

# jsjsh