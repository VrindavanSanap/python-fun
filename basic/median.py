

test_list = [4,3,5,6,7,8]

def median(numbers):
  if len(numbers)%2 == 1:
    mid_index = int(len(numbers)/2) 
    return sorted(numbers)[mid_index]
 

  if len(numbers)%2 == 0:
    mid_index = int(len(numbers)/2)  
    return (sorted(numbers)[mid_index] + sorted(numbers)[mid_index+1])/2

print(median(test_list))

print(test_list)
