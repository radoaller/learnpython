num_cats = input("How many cats do you have? ")
try:
    if int(num_cats) <= 4 and int(num_cats) >= 0:
        print ('You dont have that many cats.')
    elif int(num_cats) < 0:
        print ('That\'s not right.')
    else:
        print ('You have so many cats!')
except ValueError:
    print ('You did not enter a number. ')

#comment goes here