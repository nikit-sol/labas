n = int(input("Введите количество чисел n: "))

# Инициализируем переменные для подсчета
total_sum = 0
positive_count = 0
max_value = None  # Инициализируем None, чтобы корректно переопределить первым числом

for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    
    # Считаем общую сумму
    total_sum += num
    
    # Считаем количество строго положительных чисел (> 0)
    if num > 0:
        positive_count += 1
        
    # Инициализируем или обновляем максимум
    if max_value is None or num > max_value:
        max_value = num

print(f"Сумма {total_sum}, положительных {positive_count}, максимум {max_value}")
