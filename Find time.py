# Measuring time in x hours.

time_now = int(input('Please input the time now in HHMM format '))
hours = int(input('Enter the number of hours to be added '))
hours_digital = hours * 100
total_hours = hours_digital + time_now

time_later = (total_hours % 2400)

if time_later < 60:
    time_later = '00' + str(time_later)
elif time_later > 60 and time_later < 1200:
    time_later = '0'+ str(time_later)
else:
    time_later = time_later

print ('The time in ' + str(hours) + ' hours will be ' + str(time_later))