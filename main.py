'''
# if / else conditional statement

if (CONDITION):
  if (CONDITION):
    BODY
  elif (CODNTION):
    BODY
  else:
    BODY

else:
  BODY

# if / elif / else conditional statement

if (CONDITION):
  BODY
elif (CONDITION):
  BODY
.
.
else:
  BODY
'''

x = y = 10

if (x < y): # False
  print ("x is less than y")
else:
  if (x > y): # False
    print ("x is greater than y")
  else:
    print ("x and y must be equal")

# Exercise: Evaluate if your number is
# 1) positive/negative/zero and 
# 2) even/odd

# Variable - User number
num = int(input("Enter a number: "))

# Positive
if (num > 0):
  print ("Positive")

  # Even
  if (num % 2 == 0):
    print ("Even")

  # Odd
  elif (num % 2 == 1):
    print ("Odd")

# Negative
elif (num < 0):
  print ("Negative")

  # Even
  if (num % 2 == 0):
    print ("Even")

  # Odd
  elif (num % 2 == 1):
    print ("Odd")

# Zero
elif (num == 0):
  print ("Zero and Even")

# First ask the user for 2 numbers 
x = int(input("Please give me an x value: ")) 
y = int(input("Please give me a y value: "))

# Using a nested conditional, output which quadrant they are in 
# x = 4
# y = - 4
if(x > 0):
  if(y > 0): 
    print("Your number is in the first quadrant")
  elif(y < 0): 
    print("Your number is in the fourth quadrant")
elif(x < 0): 
  if(y > 0): 
    print("Your number is in the second quadrant")
  elif(y < 0): 
    print("Your number is in the third quadrant")

if(y == 0 and x == 0): 
  print("You are on the origin")
