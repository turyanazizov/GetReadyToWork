#Find all even elements
def even_elements(list):
  if len(list)==1:
    return (list[0]%2==0)*list
  else:
    return (list[0]%2==0)*[list[0]]+ even_elements(list[1:])

print(even_elements([1,4,53,6,36,3,7,0,2,6]))