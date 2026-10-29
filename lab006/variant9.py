# Ввод целых чисел одной строкой через пробел
input_str = input("Введите целые числа одной строкой: ")

# Преобразование строки в список целых чисел
all_numbers = [int(x) for x in input_str.split()]

# Выборка значений по условию (ненулевые числа, то есть x != 0)
matching_numbers = [x for x in all_numbers if x != 0]

# Создание отсортированной по возрастанию копии
sorted_copy = sorted(matching_numbers)

# Вычисление количества и суммы
count = len(matching_numbers)
total_sum = sum(matching_numbers)

# Вывод результатов в требуемом формате
print(f"Результат в исходном порядке: {matching_numbers}")
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
print(f"Сортированная копия: {sorted_copy}")
