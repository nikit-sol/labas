a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if a < b:
    # Шаг +1 для возрастания
    for i in range(a, b + 1):
        print(i)
elif a > b:
    # Шаг -1 для убывания
    for i in range(a, b - 1, -1):
        print(i)
else:
    # Если числа равны
    print(a)
