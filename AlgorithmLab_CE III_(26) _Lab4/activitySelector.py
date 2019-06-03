start = list(map(int,input().split()))
finish = list(map(int,input().split()))

sortedactivity = sorted(zip(finish,start))

activity = [sortedactivity[0]]
k = 1

for m in range (1,len(start)):
    if (sortedactivity[m][1]) >= (sortedactivity[k][0]):
        activity.append(sortedactivity[m])
        k = m
print(activity)
