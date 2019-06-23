
def recursiveActivitySelector(s,f,k,n):
    m=k+1
    
    while m<n and s[m]<f[k] and k>=0:
        m=m+1
        
    if m<n:
        A.append(m)
        RecursiveActivitySelector(s,f,m,n)
    else:
        return None

    return A    

s=[1,5,6,7,4,8]
f=[2,8,5,3,6,7]
A=[]                          
G=recursiveActivitySelector(s,f,-1,len(f))
print(G)


    
    
    
