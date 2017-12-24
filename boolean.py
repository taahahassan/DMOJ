x = input().split(" ")

while x.count("not") % 2 == 0:
  if "True" in x:
    print ("True")
  else:
    print ("False")
  break

while x.count("not") % 2 != 0:
  if "True" in x:
    print("False")
  else:
    print ("True")
  break
