

d = {}

d["CU"] = "see you"
d[":-)"] = "I'm happy"
d[":-("] = "I'm unhappy"
d[";-)"] = "wink"
d[":-P"] = "stick out my tongue"
d["~.~"] = "sleepy"
d["TA"] = "totally awesome"
d["CCC"] = "Canadian Computing Competition"
d["CUZ"] = "because"
d["TY"] = "thank you"
d["YW"] = "you're welcome"
d["TTYL"] = "talk to you later"

while (True):
  N = input()
  if (N in d.keys()):
    print(d[N])
  else:
    print(N)
  if (N == "TTYL"):
    break
