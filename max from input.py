a = int(input("Please input the first number."))
b = int(input("Please input the second number."))
c = int(input("Please input the third number."))

my_list = [a, b, c]
max_number = my_list[0]

for element in my_list:
    if my_list[0] < element:
        max_number = element

print ('The biggest number is', max_number)
