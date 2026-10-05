order_name=input('Введите заголовок заказа:')
cus_name=input('Введите имя:')
name1=input('Введите название первого товара:')
kol_tov1=int(input('Введите количество товара:'))
price1=float(input('Введите цену товара:'))
name2=input('Введите название второго товара:')
kol_tov2=int(input('Введите количество товара:'))
price2=float(input('Введите цену товара:'))
dostavka=int(input('Введите стоимость доставки:'))
summa=float(input('Введите внесенную сумму:'))
cost1=kol_tov1*price1
cost2=kol_tov2*price2
bezdost=cost1+cost2
sdost=cost1+cost2+dostavka
obshkol=kol_tov1+kol_tov2
sdacha=summa-sdost
print('Заказ:'+order_name+'. '+'Имя клиента:'+cus_name+'. ')
print('Название:'+name1+'. '+'Количество:'+str(kol_tov1)+'. '+'Цена:'+str(price1)+'. ' +'Стоимость:'+str(cost1)+'. ')
print('Название:'+name2+'. '+'Количество:'+str(kol_tov2)+'. '+'Цена:'+str(price2)+'. ' +'Стоимость:'+str(cost2)+'. ')
print('Общая сумма с доставкой:'+str(sdost)+'. '+'Общее количество товара:'+str(obshkol)+'. '+'Сдача:'+str(sdacha)+'. ')
