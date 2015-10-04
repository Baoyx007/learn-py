_author__ = 'haven'


def my_pow(x, n=2):
    while n > 1:
        x *= x
        n -= 1
    return x


# print(my_pow(5, 3))

def fact(n):
    if n <= 1:
        return 1
    return fact(n - 1) * n


def fact_iter(num, product=1):
    if num == 1:
        return product
    return fact_iter(num - 1, product * num)

# print(fact_iter(1000))


# print(fact(10000))
def mov(n,a='a',b='b',c='c'):
    if n==0:
        return
    mov(n-1,a,c,b)
    print(a,'->',c)
    mov(n-1,b,a,c)


mov(3)
