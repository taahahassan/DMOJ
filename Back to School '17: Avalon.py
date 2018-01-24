G = int(input())

p,e = input(),input()

result = p.split(sep=" ", maxsplit=G)
result1 = e.split(sep=" ", maxsplit = G)

result = map(float,result)
result1 = map(float,result1)


x = []

for i in p:
  y = int(p.index(i))
  x.append(float(float(e[y])/float(p[y])))

product = 1

for z in x:
  product *= z

print (product)  
