N = input()

lower_count = 0
upper_count = 0

for letter in N:
  if letter.isupper():
    upper_count = upper_count + 1
  elif letter.islower():
    lower_count = lower_count + 1

if upper_count > lower_count:
  x = print(N.upper())
if lower_count > upper_count:
  print (N.lower())
if lower_count == upper_count:
  print (N)


  
