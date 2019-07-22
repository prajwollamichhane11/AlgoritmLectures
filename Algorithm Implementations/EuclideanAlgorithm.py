def gcd(a,b):
    if a>b:
        max = a
        min = b
    else:
        max = b
        min = a
    while min != 0:
        temp = min
        min = max % min
        max = temp
    return max

a,b = map(int,input().split())
print(gcd(a,b))
