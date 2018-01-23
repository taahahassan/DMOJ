w = float(input())
h = float(input())

BMI = (w)/(h**2)

if int(BMI) > 25:
  print ("Overweight")
elif 18.5 <= BMI <=25:
  print ("Normal weight")
else:
  print ("Underweight")
