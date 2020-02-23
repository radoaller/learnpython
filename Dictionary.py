# myClass = {'Name:': 'Rashad', 'Age:': 28, 'Grade:': 'A'}

# # for (k, y) in myClass.items():
# #     print (k, y)

# # for y in myClass.keys():
# #     print (y)

# print (myClass.get ('Name:', 'Not there'))

trip_2020 = {'Food': 'Oranges', 'Entertainment': 'Movies'}

if 'Drinks' not in trip_2020:
    trip_2020['Drinks'] = 'Coke'

trip_2020.setdefault('Apparel', 'Blanket')
#print (list(trip_2020.items()))

print ('I am bringing to the trip', trip_2020.get ('napkins', 'nothing.'))
print ('Actually, I just remembered. I am bringing', list(trip_2020.values()))