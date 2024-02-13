import os
from time import sleep


print('\n\n\n')
# Need to display pattern
# Display board postion to user 
# Ask first user choice
# Need to get user input
# Clear the existing pattern
# Updated the pattern based on the user input
# Validate if three inputs are done


pattern = {1: '- - - - - -', 2: '           ', 3: '|', 4:'     .     ', 5:'     O     ', 6:'     X     ' }

number_pattern = {1: '- - - - - -', 2: '           ', 3: '|', 4:'     .     ', 5:'     0     ', 6:'     x     ',
                  11:'     1     ',22:'     2     ',33:'     3     ',44:'     4     ',
                  55:'     5     ',66:'     6     ',77:'     7     ',88:'     8     ',
                  99:'     9     ',}

board = {4:[1,3,1,3,1], 1:[4,3,4,3,4], 
         5:[1,3,1,3,1], 2:[4,3,4,3,4], 
         6:[1,3,1,3,1], 3:[4,3,4,3,4],
         7:[1,3,1,3,1]
        }

postionBoard = {4:[1,3,1,3,1], 1:[11,3,22,3,33], 
         5:[1,3,1,3,1], 2:[44,3,55,3,66], 
         6:[1,3,1,3,1], 3:[77,3,88,3,99],
         7:[1,3,1,3,1]
        }

winning_pattern = [[1, 5, 9], [3, 5, 7], [1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [9, 5, 1], [7, 5, 3], [3, 2, 1], [6, 5, 4], [9, 8, 7], [1, 4, 7],
                      [2, 5, 8], [3, 6, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3]]

user_confirmation = 'No'
user_input = 5
first_user_pattern = 5
second_user_pattern = 6
first_user_input = []
second_user_input = []
first_user_turn = False
game_end = False
winner = ''


# Function to display the board
def DisplayBoard(board, pattern):
    os.system('clear')
    for value in board.values():
        for num in value:
            print(pattern[num], end='')
        print('\n')

def GetGameInput(user):
    is_valid_input = False
    valid_input_list = [1,2,3,4,5,6,7,8,9]

    while not is_valid_input:
        print(f'\n {user}\'s input:.....', end='')
        temp = input('\t')
        if temp.isdigit():
            temp_input = int(temp)
            if temp_input in first_user_input or temp_input in second_user_input:
                print('Should enter value for free space')
                continue
            if temp_input in valid_input_list:
                is_valid_input = True
                return temp_input
        else:
            continue

def CheckWinner():
    if len(first_user_input)+len(second_user_input) == 9:
        return 'game_over'
    for each_item in winning_pattern:
        first_user_check = all(item in first_user_input for item in each_item)
        if first_user_check:
            return 'first_user'
        
        second_user_check = all(item in second_user_input for item in each_item)

        if second_user_check:
            return 'second_user'


    return None
            


def UpdateBoard(user_input, user_pattern):

    match user_input[-1]:
        case 1:
            board[1][0] = user_pattern
        case 2:
            board[1][2] = user_pattern
        case 3:
            board[1][4] = user_pattern
        case 4:
            board[2][0] = user_pattern
        case 5:
            board[2][2] = user_pattern
        case 6:
            board[2][4] = user_pattern
        case 7:
            board[3][0] = user_pattern
        case 8:
            board[3][2] = user_pattern
        case 9:
            board[3][4] = user_pattern
        
    return 


    # if user_input[-1] in [1,2,3]:
    #     if user_input[-1] == 1:
    #         board[1][0] = user_pattern
    #     elif user_input[-1] == 2:
    #         board[1][2] = user_pattern
    #     elif user_input[-1] == 3:
    #         board[1][4] = user_pattern
    
    # if user_input[-1] in [4,5,6]:
    #     if user_input[-1] == 1:
    #         board[2][0] = user_pattern
    #     elif user_input[-1] == 2:
    #         board[2][2] = user_pattern
    #     elif user_input[-1] == 3:
    #         board[2][4] = user_pattern

    # if user_input[-1] in [7,8,9]:
    #     if user_input[-1] == 1:
    #         board[3][0] = user_pattern
    #     elif user_input[-1] == 2:
    #         board[3][2] = user_pattern
    #     elif user_input[-1] == 3:
    #         board[3][4] = user_pattern

os.system('clear')


print('\n\n')
print('RULES:')
print('\t * Find the board pattern below, Have to enter the input based on teh postion number based on the positin given in pattern')
print('\t * At first, First user have to choose the symbol user')
print('\t * After symbol selection, First user would be considerd as symbol selected user. So, they have to enter input First')
print('\t * On winning we will notify you who win')
print('Enjoy the Game!! Have Fun!')
print('\n\n')



sleep(4)

DisplayBoard(postionBoard, number_pattern)



while user_confirmation != 'Yes':
    user_confirmation = input('Is Board postion is clear and shall we move to next step? Say Yes or No: \t')



while user_input != 1 and user_input != 0:
    print('\nChoose the symbol,')
    print('\t * Say 0 to choose "O"')
    print('\t * Say 1 to choose "X"')
    temp = user_confirmation = input('\t')
    if temp.isdigit():
        user_input = int(temp)

first_user_turn = True

if user_input == 0:
    first_user_pattern = 5
    second_user_pattern = 6
else:
    first_user_pattern = 6
    second_user_pattern = 5


print('Okay, here you Go!!!')

print('First user symbol', pattern[first_user_pattern] )
print('Second user symbol', pattern[second_user_pattern] )

while not game_end:
    if first_user_turn:
        # temp = GetGameInput('First User')
        first_user_input.append(GetGameInput('First User'))
        UpdateBoard(first_user_input,first_user_pattern)
        DisplayBoard(board, pattern)
        first_user_turn = False

       
    else:
        second_user_input.append(GetGameInput('Second User'))
        UpdateBoard(second_user_input,second_user_pattern)
        DisplayBoard(board, pattern)
        first_user_turn = True

    check = CheckWinner()
    if check == 'first_user':
        winner = 'First User'
        game_end = True
    elif check == 'second_user':
        winner = 'Second User'
        game_end = True
    elif check =='game_over':
        game_end = True


    print(f'Good goings:', end='')
    print(f'First user inputs are --  {', '.join(map(str,first_user_input))}  and  Second user input --  {', '.join(map(str,second_user_input))}  ')

if check == 'game_over':
    print(f'Tie!! Well done both of you!')
else:
    print(f'Congrtialations {winner} !!!, You Won!!!!!!')

        















# - - - - - -|- - - - - -|- - - - - -
#            |           |
#      1     |     2     |      3    
#            |           |           
# - - - - - -|- - - - - -|- - - - - -
#            |           |           
#      4     |     5     |      6    
#            |           |           
# - - - - - -|- - - - - -|- - - - - -
#            |           |           
#      7     |     8     |      9    
#            |           |           
# - - - - - -|- - - - - -|- - - - - -   




 






print('\n\n\n')       
