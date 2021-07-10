def fib(n):
   if n <= 1:  
       return n  
   else:  
       return(fib(n-1) + fib(n-2))

n = int(input("Enter Number:"))
if n <= 0:
   print("Enter Positive Number")
else:
   for i in range(n):
       print(fib(i))