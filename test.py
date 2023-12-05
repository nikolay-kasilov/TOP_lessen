def f():
    return(23, 34, 67)
print(f())
print(f())
def f1():
    for i in (23 ,34, 67):
       yield i
s = f1()
print(s)