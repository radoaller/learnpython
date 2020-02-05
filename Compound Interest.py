#Finding the final investment (a) after (n) years, 
#for an amount (P) that is componunded 8% monthly.

P = int (input('Enter the initial investment in USD. '))
years = int(input('Enter the number of years of compound interest. '))

n = 12
r = float(0.08)
a = float (P * (1 + r / n) ** (n * years)) 

print ('The total amount in USD after ' + str(years) + ' years is $' + str(round(a, 2)))