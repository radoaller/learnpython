# All numbers are divisible by number and 1.
# Check if number is divisible by any number from 1 -> Number.

check_number = (int(input("Enter a number ")))
list_divisors = []

for element in range (1, check_number + 1):
    if check_number % element == 0:
        list_divisors.append(element)

print (list_divisors)
