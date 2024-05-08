def discount(a,b):
    res = a * b // 100
    return res

a = int(input())
b = int(input())

print(discount(a,b))