n=1

while True:
  N = int(input())
  n += N
  if n != 54 and n!= 90 and n != 99 and n != 9 and n != 40 and n != 67 and n!= 100 and n<101 and N != 0:
    print ("You are now on square " + str(n))
  elif n == 54:
    n = 19
    print ("You are now on square " + str(n))
  elif n == 90:
    n = 48
    print("You are now on square " + str(n))
  elif n == 99:
    n = 77
    print ("You are now on square " + str(n))
  elif n == 9:
    n = 34
    print("You are now on square " + str(n))
  elif n == 40:
    n = 64
    print("You are now on square " + str(n))
  elif n == 67:
    n = 86
    print("You are now on square " + str(n))
  elif n == 100:
    print("You Win!")
    break
  elif N == 0:
    print ("You Quit!")
    break
  elif n >= 101:
    n = n - N
    print ("You are now on square " + str(n))
    
    
#Second Solution, using different methods

N=1
L1 = [54,90,99,9,40,67]
L2 = [19,48,77,34,64,86]
while True:
     a=input()
     if a=="0":
          print("You Quit!")
          break
     else:
          if N+int(a)<101:
              N += int(a)
          if N in L1:
              N = L2[L1.index(N)]
          print("You are now on square " + str(N))
          if N==100:
               print("You Win!")
               break
