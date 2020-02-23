import pprint

message = 'Today is Friday. It is a rainy day.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# rjtext = pprint.pformat (count)
# print (rjtext)

pprint.pprint (count)
