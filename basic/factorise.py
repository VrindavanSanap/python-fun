def factorise(num):
  """returns factors formated as per the requirements of the assingments
     ie 10 = 2 * 5
        100 = 2 * 2 * 5 * 5
  """
  
  print(repr_list_of_factors(num, list_of_factors(num)))
def list_of_factors(num):
    
    """
    Return prime factors of a number in list in assending order
    
    Expected output
    >>lol(100)
    >>[2, 2, 5, 5]
    """

    if num == 1:
        return []
    
    for i in range(2,num+1):
        if num%i == 0:           
            return [i] + list_of_factors(int(num/i))

def repr_list_of_factors(num, list_fac):
    
    output_string = f"{num} = {list_fac[0]}" 
    for num in list_fac[1:]:
         output_string += f" * {str(num)}"

    return output_string

  
while True:
  user_input = input("Number: ")
  if user_input == "":
    break 
  try:
    z = int(user_input)
    factorise(z)
  except Exception as e:
    print(e) 
    print(f"Enter a number dumass who tf we supposed to factorise a {type(user_input)}")
    break
