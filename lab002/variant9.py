# Вариант 9 — количество билетов и билетов в пачке

total = int(input("Введите количество билетов: "))
capacity = int(input("Введите количество билетов в пачке: "))

full = total // capacity
ostat = total % capacity
units = (total + capacity - ostat) // capacity

print("Полных пачек:"+str(full))
print("Остаток:"+str(ostat))
print("Всего пачек:"+str(units))
