import lab

#** TEST 1
# matrix1.csv:
#           10000
#           01000
#           00100
#           00010
#           00001  -> (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)

file_name1 = "lab_discrete_math1/matrix1.csv" # змінна, що зберігає шлях до файлу
file_content1 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)] # змінна, що зберігає матрицю
#                                                          з файлу у вигляді відношень

test_func1 = lab.read_file(file_name1) # виклик функції читання файлу
print(f"Testing read_file() function: {test_func1 == file_content1}")
# якщо все працює, то повертається True
