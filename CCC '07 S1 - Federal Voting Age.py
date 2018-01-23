N = int(input())

for i in range(N):
  y,m,d = map(int,input().split())
  if (2007 - y > 18) or (2007 - y == 18 and m>2) or (2007 -y == 18 and m-2 == 0 and d > 27):
    print ("Yes")
  else:
    print ("No")
    
