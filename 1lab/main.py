import random

def mini_excel():
    print("Введите размеры таблицы (N x M):")
    N = int(input("Количество строк (N): "))
    M = int(input("Количество столбцов (M): "))
    
    table = []
    print(f"Сгенерированная таблица {N}x{M}:")
    
    for i in range(N):
        row = []
        for j in range(M):
            number = random.randint(1, 100)
            row.append(number)
            print(f"{number:4}", end=" ") 
        table.append(row)
        print() 

    print("Максимумы по строкам:")
    row_maximums = []
    for i, row in enumerate(table):
        row_max = max(row)
        row_maximums.append(row_max)
        print(f"Строка {i+1}: {row_max}")
    
    print("Максимумы по столбцам:")
    col_maximums = []
    for j in range(M):
        col_max = max(table[i][j] for i in range(N))
        col_maximums.append(col_max)
        print(f"Столбец {j+1}: {col_max}")
    
    print("Сумма по диагоналям:")
    if N == M: 
        main_diag_sum = sum(table[i][i] for i in range(N))
        print(f"Главная диагональ: {main_diag_sum}")
        
        secondary_diag_sum = sum(table[i][N-1-i] for i in range(N))
        print(f"Побочная диагональ: {secondary_diag_sum}")
    else:
        print("Таблица не квадратная, диагонали не считаются")
    
    print("Поиск строки с наибольшей суммой:")
    max_sum = -1
    max_sum_row_index = -1
    
    for i, row in enumerate(table):
        row_sum = sum(row)
        print(f"Строка {i+1}: сумма = {row_sum}")
        
        if row_sum > max_sum:
            max_sum = row_sum
            max_sum_row_index = i
    
    print(f"Строка с наибольшей суммой: {max_sum_row_index + 1} (сумма = {max_sum})")
    
    return table

mini_excel()
