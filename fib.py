

# # fib(n) = fin(n-1) + fib(n-2)

# a, b =0,1

# print(f'{a} {b}', end=' ') 

# for i in range(num-2):
#     c=a+b
#     print(c, end=' ')
#     a,b =b,c


# def fib(num):
#     a, b = 0, 1
#     print(f'{a} {b}', end=' ')
#     for i in range(num-2):
#         c = a + b
#         print(c, end=' ')
#         a, b = b, c

# fib(10)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# print(fib(5))

def fibonacci_series(num):
    series = []
    for i in range(num):
        series.append(fib(i))
    return series

print(fibonacci_series(10))
