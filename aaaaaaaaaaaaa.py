g1 = (x for x in range(11))
print(next(g1))
for i in g1:
    print(i)
print('---------------------------------------------------------------------------------')

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(10))
print('---------------------------------------------------------------------------------')
# 使用生成器，yield完成斐波拉契数列
def fib01(max1):
    a = 0
    b = 1
    for i in range(max1):
        tuple01 = (a, b)
        yield tuple01[1]
        a = tuple01[1]
        b = tuple01[0]+tuple01[1]
    return 'None'
f01 = fib01(10)
for i in f01:
    print(i)
print('---------------------------------------------------------------------------------')
# generator方法得不到返回值
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
while True:
    try:
        x = next(f01)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break