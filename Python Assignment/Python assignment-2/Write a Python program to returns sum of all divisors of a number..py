# Write a Python program to returns sum of all divisors of a number

num = int(input("Enter a number: "))

divisor_sum = 0

# Iterate from 1 to the number (inclusive)
for i in range(1, num + 1):
    # Check if i is a divisor of the number
    if num % i == 0:
        divisor_sum += i

print(f"The sum of divisors of {num} is: {divisor_sum}")
