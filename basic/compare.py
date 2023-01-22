def checkQ(q):
  if q == 'q' or q =="Q":
   return True

def compare(a, b):
  """
  returns string stating the comparison between numbers 
  a and b 

  Expected output
  >>compare(10, 29):
  >>10 is smoller than 29
  """
 
  if a > b: return f"{a} is BIGGER than {b} \n"
  elif a < b: return f"{a} is smoller than {b} \n"
  elif a == b: return f"{a} is Equal to {b} \n"


print("press q to quit \n")

while True:
  num1 = input("1st Number: ") 
  if checkQ(num1): break
  num2 = input("2st Number: ")
  if checkQ(num2): break
  print() 
  print(compare(num1, num2))
  
