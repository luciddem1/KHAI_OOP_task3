import math

def main():
    print("Практична робота №3 Степан Васильєв 312ст")  # Виведення інформації про практичну роботу та ім'я та групу студента
    task1()  
    newtask()  
    task2('D:\ХАІ\стьопа\ООП\lab3\matrix.txt')  
 

def newtask():  # Функція введення роздільної лінії та чекання введення користувача перед продовженням програми
    print("\n\n====================================================================================================================================================\n\n")
    input() 

def task1():
    """Введення даних, виклик функції знаходження мінімуму та максимуму, виведення результатів."""
    # Введення даних
    A = float(input("Введіть число A: "))
    B = float(input("Введіть число B: "))
    C = float(input("Введіть число C: "))
    D = float(input("Введіть число D: "))
    
    # Знаходження мінімального та максимального значення
    min_value, max_value = find_minmax_for_ABCD(A, B, C, D)
    
    # Виведення результатів
    print(f"Мінімальне значення: {min_value}")
    print(f"Максимальне значення: {max_value}")

def Minmax(X, Y):
    """Записує мінімальне значення у X та максимальне у Y."""
    if X > Y:
        X, Y = Y, X
    return X, Y

def find_minmax_for_ABCD(A, B, C, D):
    """Знаходить мінімальне і максимальне значення серед чотирьох чисел."""
    # Знаходимо мінімум для A та B
    min_AB, _ = Minmax(A, B)
    
    # Знаходимо максимум для C та D
    _, max_CD = Minmax(C, D)
    
    # Знаходимо мінімум та максимум для min_AB та max_CD
    overall_min, overall_max = Minmax(min_AB, max_CD)
    
    return overall_min, overall_max



def read_matrix_from_file(file_path):
    """Зчитати матрицю з текстового файлу."""
    with open(file_path, 'r') as file:
        matrix = [[int(num) for num in line.split()] for line in file]
    return matrix

def find_min_max_elements(matrix):
    """Знайти мінімальний і максимальний елемент в кожному рядку матриці."""
    min_max_elements = [(min(row), max(row)) for row in matrix]
    return min_max_elements

def find_min_max_rows(min_max_elements):
    """Знайти рядки з найменшим і найбільшим елементами."""
    min_element_row = min(range(len(min_max_elements)), key=lambda i: min_max_elements[i][0])
    max_element_row = max(range(len(min_max_elements)), key=lambda i: min_max_elements[i][1])
    return min_element_row, max_element_row

def swap_rows(matrix, row1, row2):
    """Поміняти місцями рядки матриці."""
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def write_matrix_to_file(matrix, file_path):
    """Записати матрицю у текстовий файл."""
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def task2(file_path):
    """Виконати операції для Matrix 7."""
    # Зчитати матрицю з файлу
    matrix = read_matrix_from_file(file_path)
    
    # Знайти мінімальний і максимальний елемент в кожному рядку
    min_max_elements = find_min_max_elements(matrix)
    
    # Знайти рядки з найменшим і найбільшим елементами
    min_element_row, max_element_row = find_min_max_rows(min_max_elements)
    
    # Поміняти місцями рядки з найменшим і найбільшим елементами
    swap_rows(matrix, min_element_row, max_element_row)
    
    # Записати змінену матрицю у файл
    write_matrix_to_file(matrix, file_path)

main()