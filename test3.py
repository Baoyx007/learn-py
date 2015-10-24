__author__ = 'haven'


def calcDistance(A, B, C, D):
    # write code here
    sum = A + B + C + D
    return sum*4-sum


def calcOne(n):
    if n <= 0:
        return 0
    else:
        return n*2 + calcOne(n // 2)


print(calcDistance(100, 90, 80, 70))
