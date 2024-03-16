# Function to convert binary to decimal
def binary_to_decimal(binary):
 decimal = int(binary, 2) 
# Using int() function with base 2 to convert binary to decimal
 return decimal
# Function to convert octal to hexadecimal
def octal_to_hexadecimal(octal):
 decimal = int(octal, 8) 
# Using int() function with base 8 to convert octal to decimal
 hexadecimal = hex(decimal) 
# Using hex() function to convert decimal to hexadecimal
 return hexadecimal
# Taking user input for binary number
binary_num = input("Enter a binary number: ")
# Calling binary_to_decimal function and storing the result
decimal_num = binary_to_decimal(binary_num)
# Taking user input for octal number
octal_num = input("Enter an octal number: ")
# Calling octal_to_hexadecimal function and storing the result
hexadecimal_num = octal_to_hexadecimal(octal_num)
# Output
print("Decimal equivalent of binary", binary_num, "is:", decimal_num)
print("Hexadecimal equivalent of octal", octal_num, "is:", hexadecimal_num)
