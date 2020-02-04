a = [1, 2, 3, 6, 7, 9, 12, 10, 11, 4, 5, 8, 4]
result = []

for element in a:
    if element == 4:
        continue
    if element < 5:
        result.append (element)

print ("This list has", (len(result)), "numbers. These numbers are:", result, end=".")
