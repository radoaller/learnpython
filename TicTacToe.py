import pprint

the_board = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'MM': ' ', 'MR': ' ', 'BL': ' ', 'BM': ' ', 'BR': ' '}
#pprint.pprint(the_board)

def graphic_board (board):
    print (board['TL'], '|', board['TM'], '|', board['TR'])
    print ('---------')
    print (board['ML'], '|', board['MM'], '|', board['MR'])
    print ('---------')
    print (board['BL'], '|', board['BM'], '|', board['BR'])

graphic_board(the_board)
    