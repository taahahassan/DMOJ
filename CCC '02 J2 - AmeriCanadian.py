N = input().split(',')

for word in N:
  if "or" in word and len(word) > 4:
    words = word.replace("or","our")
  if word == "quit!":
    raise SystemExit

print (words)
