import main_tic

#currentPlayer = "⛝"
#isGameRunning = True
#board = ["⛶", "⛶", "⛶",
#        "⛶", "⛶", "⛶", 
#        "⛶", "⛶", "⛶"]

currentPlayer = "⛝"

def game():
    
    isGameRunning = True
    board = ["⛶", "⛶", "⛶",
            "⛶", "⛶", "⛶", 
            "⛶", "⛶", "⛶"]



    def grid(board): 
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])




    def playerInput(board, currentPlayer):
        inp = int(input("Enter a number 1-9 "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "⛶":
            board[inp-1] = currentPlayer
            

        elif inp >= 1 and inp <= 9 and board[inp-1] == currentPlayer:
            print("Slot already taken.")
        
    def switchPlayer():
        global currentPlayer
        if currentPlayer == "⛝":
            currentPlayer = "⛋"
            print("⛋'s Turn")
        else:
            currentPlayer = "⛝"
            print("⛝'s Turn")


    def IsWinHorizontal(board):
        if board[0] == board[1] == board[2] and board[0] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False
        elif board[3] == board[4] == board[5] and board[3] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False
        elif board[6] == board[7] == board[8] and board[6] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False

    def IsWinVertical(board):
        if board[0] == board[3] == board[6] and board[0] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False
        elif board[1] == board[4] == board[7] and board[1] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False
        elif board[2] == board[5] == board[8] and board[2] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False

    def IsWinDiagonal(board):
        if board[0] == board[4] == board[8] and board[0] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False
        elif board[3] == board[4] == board[6] and board[3] == currentPlayer:
            grid(board)
            print("Winner:", currentPlayer)
            main_tic.main()
            isGameRunning = False
    
    def IsTie(board):
        if "⛶" not in board:
            grid(board)
            print("Tie.")
            main_tic.main()
            isGameRunning = False



   






    while isGameRunning:
        grid(board)
        playerInput(board,currentPlayer)
        IsWinHorizontal(board)
        IsWinVertical(board)
        IsWinDiagonal(board)
        IsTie(board)
        switchPlayer()
