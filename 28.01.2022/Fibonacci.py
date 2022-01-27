#Function to implement Fibonacci Series
def Fibonacci(N):
   if N <= 1:
       return N
   else:
       return(Fibonacci(N-1) + Fibonacci(N-2))

#Number of terms to be printed
number = 10
if number <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(number):
       print(Fibonacci(i))