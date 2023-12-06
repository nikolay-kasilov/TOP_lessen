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