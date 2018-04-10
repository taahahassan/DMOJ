N, D = map(int,input().split(" "))
n = input()
result = n.split(sep=" ", maxsplit=N)



l = []
for i in result:
  i = int(i)
  if i != 0 and D % i == 0:
    l.append(
  
if len(l) == 0:
  print ("This is not the best time for a trip.")
else:
  w = max(l)
  y = int(D)/int(w)
  if y < 0:
    print (str((int(-1*y))))
  else:
    print (str((int(y))))

