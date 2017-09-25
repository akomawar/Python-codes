N,M=map(int,input().split())
print(N)
print(M)
a=[]
b=[]
c=[]
for i in range(N):
    a.append(input().split())
print(a)
K=int(input())
print(K)

c = sorted(a, key=lambda record: record[K])
print(c)
for i in c:
    print(*i)
    
