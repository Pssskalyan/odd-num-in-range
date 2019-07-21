#odd in range
l,u=map(int,input().split())
for i in range(l,u):
  if(i%2!=0 and i!=1):
    print(i,end=" ")
