'Карточка студента'
print('Введите фамилию:')
surname=input()+' '
print('Введите имя:')
name=input()+' '
print('Введите группу:')
group=str(int(input()))+' '
print('Введите город:')
city=input()+' '
print('Введите полное количество лет:')
age=str(int(input()))+' '
print('Введите любимый предмет:')
fav_subj=input()+' '
print('Введите количество часов подготовки в неделю:')
time=int(input())
eee='Имя и фамилия:'+surname+name+'Группа №'+group+'Город:'+city+'Количество полных лет:'+age+'Любимый предмет:'+fav_subj
abc='Количество часов в неделю:'+str(time)+' '+'Среднее время подготовки в день:'+str(time/7)
print(eee, abc)
