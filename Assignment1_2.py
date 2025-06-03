# Read two numbers from the console
num1 = float(input("Enter the first number (less than 100): "))
num2 = float(input("Enter the second number (less than 100): "))

# Calculate the difference
diff = abs(num1 - num2)

# Check if the difference is less than 20
if diff < 20:
    result = 2 * diff
else:
    result = diff

# Print the result
print("The difference between the numbers is:", result)
