"""Module with test for lab.py"""
import lab

#** TEST 1
# matrix1.csv:
#           10000
#           01000
#           00100
#           00010
#           00001  -> (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)

R_FILE_NAME1 = "matrix1.csv" # константа, що зберігає шлях до файлу
file_content1 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)] # змінна, що зберігає матрицю
#                                                          з файлу у вигляді відношень

test_func1 = lab.read_file(R_FILE_NAME1) # виклик функції читання файлу
print(f"Testing read_file() function: {test_func1 == file_content1}")
# якщо все працює, то повертається True

#** TEST 2

W_FILE_NAME1 = "matrix2" # константа, що зберігає назву файлу, що буде створено
R_FILE_NAME2 = "matrix2.csv" # константа, що зберігає шлях до файлу
relations2 =[(1,1), (2,2), (3,3), (4,4), (5,5)] # змінна, що зберігає матрицю
#                                                 для тесту у вигляді відношень
SIZE1 = 5 # константа, що зберігає розмір матриці на випадок,
#           якщо матриця повністю чи певною мірою складається з нулів

lab.write_file(W_FILE_NAME1, relations2, SIZE1) # виклик функції записування файлу

test_func2 = lab.read_file(R_FILE_NAME2)

print(f"Testing write_file() function: {test_func2 == relations2}")
# якщо все працює, то файл має бути створеним під відповідним іменем і повертається True



#** TEST 3

W_FILE_NAME2 = "matrix3" # константа, що зберігає назву файлу, що буде створено
R_FILE_NAME3 = "reflexive_matrix3.csv" # константа, що зберігає шлях до файлу
relations3 = [(1,2), (1,3), (2,3), (3,1)] # змінна, що зберігає матрицю
#                                           для тесту у вигляді відношень
SIZE2 = 3 # константа, що зберігає розмір матриці на випадок,
#           якщо матриця повністю чи певною мірою складається з нулів

lab.find_reflexive_closing(relations3, W_FILE_NAME2, SIZE2) # виклик функції записування файлу

reflexive_relations = [(1,1), (1,2), (1,3), (2,2), (2,3), (3,1), (3,3)] # список відношень,
#                                                                         що репрезентують
#                                                                         рефлексивно замкнуту
#                                                                         матрицю
test_func3 = lab.read_file(R_FILE_NAME3)

print(f"Testing find_reflexive_closing() function: {test_func3 == reflexive_relations}")
# якщо все працює, то файл має бути створеним під іменем "reflexive_{назва_файлу_з_константи}"
# і повертається True

#** TEST 4

W_FILE_NAME3 = "matrix4" # константа, що зберігає назву файлу, що буде створено
R_FILE_NAME4 = "symmetrical_matrix4.csv" # константа, що зберігає шлях до файлу
relations4 = [(1,2), (1,3), (2,3), (3,1)] # змінна, що зберігає матрицю
#                                           для тесту у вигляді відношень
SIZE3 = 3 # константа, що зберігає розмір матриці на випадок,
#           якщо матриця повністю чи певною мірою складається з нулів

lab.find_symmetrical_closing(relations4, W_FILE_NAME3, SIZE3) # виклик функції записування файлу

symmetrical_relations = [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)] # список відношень,
#                                                                         що репрезентують
#                                                                         симетрично замкнуту
#                                                                         матрицю
test_func4 = lab.read_file(R_FILE_NAME4)

print(f"Testing find_symmetrical_closing() function: {test_func4 == symmetrical_relations}")
# якщо все працює, то файл має бути створеним під іменем "symmetrical_{назва_файлу_з_константи}"
# і повертається True


#** TEST 5

W_FILE_NAME4 = "matrix5" # константа, що зберігає назву файлу, що буде створено
R_FILE_NAME5 = "transitive_matrix5.csv" # константа, що зберігає шлях до файлу
relations5 =[(1,1), (1,2), (2,2), (2,3), (3,3), (3,4), (4,4), (5,5)] # змінна, що зберігає матрицю
#                                                                      для тесту у вигляді відношень
SIZE4 = 5 # константа, що зберігає розмір матриці на випадок,
#           якщо матриця повністю чи певною мірою складається з нулів

lab.find_transitive_closing(relations5, W_FILE_NAME4, SIZE4) # виклик функції записування файлу

transitive_relations = [(1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,3), (3,4), (4,4), (5,5)]
#                                                                           список відношень,
#                                                                           що репрезентують
#                                                                           транзитивно замкнуту
#                                                                           матрицю
test_func5 = lab.read_file(R_FILE_NAME5)

print(f"Testing find_transitive_closing() function: {test_func5 == transitive_relations}")
# якщо все працює, то файл має бути створеним під іменем "transitive_{назва_файлу_з_константи}"
# і повертається True

#** TEST 6

relations6 = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,4)] # еквіваленція для чогось
size6 = 4
expected_result6 = [[0, 1, 2], [3]]

test_func6 = lab.find_equivalence_classes(relations6, size6) # виклик функції

print(f"Testing ind_equivalence_classes() function: {test_func6 == expected_result6}")

#** TEST 7

relations7 = [(1,2), (1, 3), (2,3)] # відношення для перевірки на транзитивність
expected_result7 = True

test_func7 = lab.is_transitive(relations6) # виклик функції

print(f"Testing is_transitive() function: {test_func7 == expected_result7}")
