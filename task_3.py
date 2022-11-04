# данная программа находит разницу между максимальным и минимальным значением дробной части элементов из списка вещественных чисел. 
import random
n = int(input('введите количество элементов списка: '))
lst = [round(random.uniform(-99.999, 100), 3) for k in range(n)] # список случайных вещественных чисел
print(lst)
lst_new = [] # список для дробных частей
for i in range(n):
   lst_new.append(round(abs(lst[i]) % 1,3)) # добавляем в новый список дробные части чисел списка lst
print(lst_new)

min = max = lst_new[0]   # присваиваем переменным  min и max нулевой элемент списка
for i in lst_new:
   if i < min:
      min = i
   if i > max:
      max = i
diff = max - min
print('Разница между максимальным и минимальным значениями дробной части равна: ', round(diff,3))