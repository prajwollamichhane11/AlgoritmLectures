def recu_act_sel(s,f,k,n,act):
    m = k+1
    while m<n and s[m]<f[k] and k>0:
        m = m+1
    if m<=n:
        act.append(m)
        return recu_act_sel(s,f,m,n,act)
        return act


s = []
f = []
start = list(map(int,input().split()))
finish = list(map(int,input().split()))
n = len(start)

sortedactivity = sorted(zip(finish,start))

for i in range(n):
    s.append(sortedactivity[i][1])
    f.append(sortedactivity[i][0])
act = []
k = -1
recu_act_sel(s,f,k,n,act)
print(act)
sortedactivity = list(zip(s,f))
for i in range(len(act)-1):
    print(sortedactivity[act[i]])
