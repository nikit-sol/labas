rejected_count = 0

while True:
    num = int(input("Введите положительное число: "))
    
    if num > 0:
        # Если число положительное — выходим из цикла
        break
    else:
        # Если ноль или отрицательное — отклоняем попытку
        rejected_count += 1

# Вывод результатов после успешного ввода
print(f"Квадрат {num ** 2}, отклонено {rejected_count}")
