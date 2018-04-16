import array 


def board(n):
    
    if n == 1:
        return [1, 2, 3]
    elif n == 2:
        return [4, 5, 6]
    elif n == 3:
        return [7, 8, 9]
    	
    
def draw_board():
    for x in range(1, 4):
        print(board(x))

def main():
    print("Welcome to ISAT252 Tic-Tac-Toe game!")
    print("Here is the game board: ")
    draw_board()

if __name__ == '__main__':
    main()
    	