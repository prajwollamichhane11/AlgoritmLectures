act = [a[m]]

def recu_act_sel(s,f,k,n):
    m = k+1
    while m<=n and s[m]<f[k]:
        m = m+1
    if m<=n:
        return act.append(recu_act_sel(s,f,m,n))
    else:
        return act

s = []
f = []
n = len(s)
start = list(map(int,input().split()))
finish = list(map(int,input().split()))

sortedactivity = sorted(zip(finish,start))

for i in range(n):
    s = s.append(sortedactivity[i][1])
    f = f.append(sortedactivity[i][0])

k = 0
print(recu_act_sel(s,f,k,n))
