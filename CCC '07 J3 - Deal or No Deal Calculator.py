N = int(input())

data = input()

result = data.split(sep=" ", maxsplit=N)
result = map(int,result)
offer = int(input())

d = {
  1:100,
  2:500,
  3:1000,
  4:5000,
  5:10000,
  6:25000,
  7:50000,
  8:100000,
  9:500000,
  10:1000000
}

h = []

for i in result:
  h.append(float(d[i]))


h = sum(i for i in h)

f = sum(d.values())

g = (f-h)/N


if g > offer:
  print ("no deal")
else:
  print ("deal")
