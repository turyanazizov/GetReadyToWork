#Find all even elements
def even_elements(l):
  if len(l)==1:
    return (l[0]%2==0)*l
  else:
    return (l[0]%2==0)*[l[0]]+ even_elements(l[1:])

print(even_elements([1,4,53,6,36,3,7,0,2,6]))