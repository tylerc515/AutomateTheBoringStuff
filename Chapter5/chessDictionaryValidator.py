# currentChessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# bad position
# currentChessBoard = {'16h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# 2 black kings
# currentChessBoard = {'1h': 'bking', '6c': 'bking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# 9 pawns
currentChessBoard = {'6h': 'wpawn', '6c': 'wpawn', '2g': 'wpawn', '5h': 'wpawn', '3e': 'wpawn',
                     '8b': 'wpawn', '7f': 'wpawn', '6e': 'wpawn', '4h': 'wpawn'}

isValid = False

def isValidChessBoard(chessBoard):

    chessBoardValuesList = list(chessBoard.values())
    
    validSpaces = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
                   '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
                   '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
                   '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
                   '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
                   '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
                   '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
                   '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']
    
    validPieces = ['wking', 'wqueen', 'wrook', 'wbishop', 'wknight', 'wpawn',
                   'bking', 'bqueen', 'brook', 'bbishop', 'bknight', 'bpawn']
    
    wKingCount = chessBoardValuesList.count('wking')
    bKingCount = chessBoardValuesList.count('bking')
    wPawnCount = chessBoardValuesList.count('wpawn')
    bPawnCount = chessBoardValuesList.count('bpawn')
    blackLetter = 'b'
    whiteLetter = 'w'
    whiteTotalCount = 0
    blackTotalCount = 0

    #determine if the first letter is b or w, and count the totals for each player.
    for i in chessBoard.values():
        #ensure all peices are valid pieces
        if i in validPieces:
            for letter in i[0]:
                if letter == blackLetter:
                    blackTotalCount += 1
                elif letter == whiteLetter:
                    whiteTotalCount += 1
        else:
            return False
    if whiteTotalCount <= 16 and blackTotalCount <= 16:
        #If the totals for each player are less than 16, then count the number of kings
        #and pawns and validate
        if wKingCount == 1 and bKingCount == 1 and wPawnCount < 8 and bPawnCount < 8:
            isValid = True
        else:
            return False
    #ensure all pieces are on a valid space
    for i in chessBoard.keys():
        if i in validSpaces:
            isValid = True
        else:
            return False
    

    return(isValid)

if isValidChessBoard(currentChessBoard) == True:
    print('This is a valid chess board.')
else:
    print('This is NOT a valid chess board.')