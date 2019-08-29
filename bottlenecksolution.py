b=int(input())
a = eval(input())
count=[]
for i in range(b):
    c=0
    for j in range(b):
        if (a[i]==a[j]):
            c=c+1
    count.append(c)
print(max(count))
