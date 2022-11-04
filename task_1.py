# данная программа находит сумму элементов заданного списка, стоящих на нечётных позициях
from random import randint
n = int(input('введите количество элементов списка: '))
if n <= 0:
   print('вы ввели некорректное число')
   exit() 
lst = [randint(-100, 100) for i in range(n)]
print('список: ', lst)
sum = 0
for i in range(1,n,2):
   sum += lst[i]
print('сумма элементов на нечетных позициях равна ', sum)