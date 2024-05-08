def farm(chic,cow,pig):
    chic*=2
    cow*=4
    pig*=4
    res = chic + cow + pig
    return res

a = int(input())
b = int(input())
c = int(input())

print(farm(a,b,c))