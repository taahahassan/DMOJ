N = input().split(',')

for word in N:
  if word != "quit!":
    print (word)
    x = len(word)
    if "or" in word: 
      if x > 4:
        words = word.replace("or","our")
  elif word == "quit!":
    quit()
  
print (N)
print (words)
