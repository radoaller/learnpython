#convert list of strings to integers

numbers = (input('Enter a number: '))
number_list= list(numbers)
sum_of_numbers = 0

for a in range(0, len(number_list)):
    number_list[a] = int(number_list[a])

for a in range(0, len(number_list)):
    sum_of_numbers += (number_list[a])
     
print(number_list)
print (sum_of_numbers)