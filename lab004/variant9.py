n = int(input("Введите количество чисел n: "))

count = 0
total_sum = 0

for i in range(n):
    num = int(input("Введите число" +str(int(i+1))+":" ))
    
    # Условие отбора: ненулевые числа
    if num != 0:
        count += 1
        total_sum += num

print("Количество" +str(count), "сумма"+str(total_sum)+":")
