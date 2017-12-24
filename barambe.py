#For some reason, DMOJ not accepting solution. Still works though.


N = input().split()

for word in N:
  for letter in word:
    if letter.isupper() and word != N[0]:
      print (".", word, end = '')
      break  
    else:
      print ("", word, end = '')
      break  
