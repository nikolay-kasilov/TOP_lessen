# test_задачки
def f():
    return(23, 34, 67)
print(f())
print(f())
def f1():
    for i in (23 ,34, 67):
       yield i
s = f1()
print(s)
# test_задачка с факториалом
def fact(n):
    pr =1
    a = []
    for i in range(1, n+1):
        pr =pr * i
        a.append(pr)
    return a
print(fact(10))
 # test_задачка таже что с верху но с помощью генератора.
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr = pr*i
        yield pr
for i in fact(10):
    print(i, end=", ")
