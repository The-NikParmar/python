# Write a Python function to check whether a number is perfect or not.
def is_perfect_number(number):
    if number <= 0:
        return False
    
    # Find divisors and sum them
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    
    # Check if the sum of divisors equals the original number
    return divisors_sum == number

num_to_check = int(input("enter no"))
if is_perfect_number(num_to_check):
    print(f"{num_to_check} is a perfect number.")
else:
    print(f"{num_to_check} is not a perfect number.")
