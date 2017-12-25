#used same code as in listminimum.py because it is same question


size = int(input()) #number of integers that need to be sorted
a = []

for i in range(0, size):
  i = int(input()) #type numbers that need to be sorted
  a.append(i)

a = sorted(a)

for i in range(0,size):
  print (a[i])
  
