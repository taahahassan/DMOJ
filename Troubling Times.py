N, D = map(int,input().split(" "))
n = input()
result = n.split(sep=" ", maxsplit=N)



l = []
for i in result:
  if D % int(i) == 0:
    l.append(i)
  
if len(l) == 0:
  print ("This is not the best time for a trip")
else:
  w = max(l)
  y = D/int(w)
  if y < 0:
    print (-1 * y)
  else:
    print (y)
