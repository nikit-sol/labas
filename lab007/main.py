from functions import select_numbers
numbers = [-5, 0, 2, 5]
threshold = int(input("Введите порог (целое неотрицательное число): "))
filtered_list = select_numbers(numbers, threshold)
print(f"Результат отбора: {filtered_list}")
