def foot_point(a,b,c):
    a*=3
    b*=1
    c*=0
    res = a + b + c
    return res

win = int(input())
draw = int(input())
lose = int(input())

print(foot_point(win,draw,lose))