def fibonacci(n):
 
 #Function to calculate the nth Fibonacci number.
 # Base case
 if n == 1:
     return 0
 elif n == 2:
     return 1
 elif n <= 0:
     return "N must be a positive integer."
 # Recursive case
 else:
     return fibonacci(n-1) + fibonacci(n-2)
# Taking input from the user
n = int(input("Enter a value for N: "))
# Calling the fibonacci function and storing the result
result = fibonacci(n)
# Checking if the result is a string (error message)
if isinstance(result, str):
 print("Invalid Input-",result)
else:
 print("The", n, "th Fibonacci number is:", result)
