def iterationActivitySelector(s,f):
    A=[0]
    n=len(s)
    k=0

    for i in range(1,n):
       if s[i]>=f[k]:
           A.append(i)
           k=i
    return A



s=[1,5,6,7,4,8]
f=[2,8,5,3,6,7]
G=iterationActivitySelector(s,f)
print(G)
           
        
    
