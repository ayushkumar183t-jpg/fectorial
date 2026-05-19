# Program to calculate the factorial of a number

# Function to calculate factorial
def factorial(number):
    result = 1

    # Loop to multiply numbers
    for i in range(1, number + 1):
        result = result * i

    return result

# Taking input from the user
num = int(input("Enter a number: "))

# Calling the function
answer = factorial(num)

# Displaying the result
print("Factorial of", num, "is:", answer)