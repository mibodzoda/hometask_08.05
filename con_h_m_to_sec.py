def convert(h,m):
    mn = h * 3600
    sec = m * 60
    res = mn + sec
    return res

h = int(input())
m = int(input())

print(convert(h,m))