X = int(input())
Y = int(input())

for i in range (X,Y+1):
  if (i-X) % 60 == 0:
    print (i)
