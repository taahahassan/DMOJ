N = int(input())

data = input()

result = data.split(sep=" ", maxsplit=N)

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
  e = int(d[i])
  h.append(e)

h = sum(i for i in h)

f = sum(d.values())

print (f)
g = (f-h)/N

print (g)
