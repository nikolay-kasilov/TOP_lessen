                           # test_Z
def f():
    return(23, 34, 67)
print(f())
print(f())
def f1():
    for i in (23 ,34, 67):
       yield i
s = f1()
print(s)
           # test_Z        С ФАКТОРИАЛОМ
def fact(n):
    pr =1
    a = []
    for i in range(1, n+1):
        pr =pr * i
        a.append(pr)
    return a
print(fact(10))
     # test_Z   ЗАДАЧА ТА ЖЕ С ПОМОЩЬЮ ГЕНЕРАТОРА
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr = pr*i
        yield pr
for i in fact(10):
    print(i, end=", ")



 #            test_Z  < ЯВЛЯЕТСЯ ЛИ ЧИСЛО ПРОСТЫМ> вар 1

a = int(input('Введите число:\n'))
k =0
for i in range(1,a +1):
    if a % i == 0:
         k += 1
if k == 2:
    print(' Число простое')
else:
    print('Число не простое')

 #            test_Z  < ЯВЛЯЕТСЯ ЛИ ЧИСЛО ПРОСТЫМ> вар 2

a = int(input('Введите число:\n'))
k = 0
delit =[]
for i in range(1, a + 1):
    if a % i == 0:
        k += 1
        delit.append(i)
if k == 2:
    print(' Число простое')
else:
    print('Число не простое')
    print('Список чисел на которые можно поделить:',delit)

                    # test_Z СУММА ЧИСЕЛ
a = int(input('Введи число:\t'))
s = 0
while a >0:
    s += a%10
    a = a//10
print(s)
                           #test_Z
sp =[7, 8, 5, 3, 7 ,4]
s1 =[]
for i in sp:
    s1.append(i**2)
print(s1)
print()
            #test_Z УБИРАЕМ ПРОБЕЛЛЫ И ОДИНАКОВЫЕ БУКВЫ

s = input('введите строку\t')
s_new = ''
for i in s:
    if i not in s_new and i != ' ':
        s_new += i
print(s_new)
                     # test_Z СЧИТАЕМ КОЛ. СЛОВ
s = input('введите строку\t')
k = 0
for x in s:
    if x ==' ':
        k += 1
print(k)
                          # test_Z СЧИТАЕМ КОЛ. СЛОВ
s = input('введите строку\t')
print(len(s.split()))

      #test_Z КАЛЬКУЛЯТОР СЧАСТЛИВЫХ ЧИСЕЛ

s = input('Введите дату рождения ДД.ММ.ГГГГ :')
s1 = s.split(".")
day = int(s1[0])
month =int(s1[1])
year =int(s1[2])
sum = 0
while day >0:
    sum +=day % 10
    day//= 10
while month  >0:
     sum += month % 10
     month//= 10
while  year >0:
    sum += year % 10
    year//= 10
sum1 =0
while   sum >0:
    sum1 +=  sum % 10
    sum//= 10
print(sum1)

import
