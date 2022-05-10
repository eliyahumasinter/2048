import random
import copy


class Game():
    def __init__(self):
        self.board =[[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

        self.score = 0
        self.newNumber()
        self.newNumber()
        self.gameOver = False
    def newNumber(self):
        empty = []
        num = random.choice([2,4])
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    empty.append([i,j])
        choice = random.choice(empty)
        newBoard = self.board
        newBoard[choice[0]][choice[1]] = num
        self.board = newBoard


    def printBoard(self):
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()


    def getNonEmptySquares(self):
        res = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] != 0:
                    res.append([i,j])
        return res


    def moveRight(self, square): 
        try:
            if self.board[square[0]][square[1]+1] == self.board[square[0]][square[1]]:
                self.board[square[0]][square[1]] = 0
                self.board[square[0]][square[1]+1] *= 2
                self.score += self.board[square[0]][square[1]+1]
                return
            elif self.board[square[0]][square[1]+1] != 0:
                return
            
            else:
                temp = self.board[square[0]][square[1]]
                self.board[square[0]][square[1]] = 0
                self.board[square[0]][square[1]+1] = temp
                square[1] += 1
                
                self.moveRight(square)
                
        except IndexError as e:
            return

    def moveLeft(self,square):
        try:
            num = self.board[square[0]][square[1]-1]
            if square[1]-1 < 0:
                raise IndexError('Number is negative')
            if num == self.board[square[0]][square[1]] and num != 0:
                self.board[square[0]][square[1]] = 0
                self.board[square[0]][square[1]-1] *= 2
                self.score += self.board[square[0]][square[1]-1]
                return
            elif self.board[square[0]][square[1]-1] != 0:
                return
            
            else:
                temp = self.board[square[0]][square[1]]
                self.board[square[0]][square[1]] = 0
                self.board[square[0]][square[1]-1] = temp
                square[1] -= 1
                self.moveLeft(square)
                
        except IndexError as e:
            return
        

    def moveUp(self,square):
        try:
            if self.board[square[0]-1][square[1]] == self.board[square[0]][square[1]]:
                self.board[square[0]][square[1]] = 0
                self.board[square[0]-1][square[1]] *= 2
                self.score += self.board[square[0]-1][square[1]]
                return
            elif self.board[square[0]-1][square[1]] != 0:
                return
            else:
                temp = self.board[square[0]][square[1]]
                self.board[square[0]][square[1]] = 0
                self.board[square[0]-1][square[1]] = temp
                square[0] -= 1
                self.moveUp(square)
        except IndexError as e:
            return

    def moveDown(self, square):
        try:
            if self.board[square[0]+1][square[1]] == self.board[square[0]][square[1]]:
                self.board[square[0]][square[1]] = 0
                self.board[square[0]+1][square[1]] *= 2
                self.score += self.board[square[0]+1][square[1]]
                return
            elif self.board[square[0]+1][square[1]] != 0:
                return
            else:
                temp = self.board[square[0]][square[1]]
                self.board[square[0]][square[1]] = 0
                self.board[square[0]+1][square[1]] = temp
                square[0] += 1
                self.moveDown(square)
        except IndexError as e:
            return

    def move(self, choice):
        
        if not self.gameOver:
            copyboard = copy.deepcopy(self.board)
            toMove = self.getNonEmptySquares() #by defualt values go left to right, top to down
            if choice == "r":
                toMove.reverse() #need values to start moving right to left, no left to right [2,0,4,0] should be [0,0,2,4] not [0,2,0,4]
                for i in toMove:
                    self.moveRight(i)
            elif choice == "l":
                for i in toMove:
                    self.moveLeft(i)
            elif choice == "u":
                for i in toMove:
                    self.moveUp(i)
            elif choice == "d":
                toMove.reverse() #same as for moving right
                for i in toMove:
                    self.moveDown(i)
            if self.board != copyboard: #1 or more tile(s) have changed position
                self.newNumber()

            
        
        
        
    def checkGameOver(self):
        nonEmptySquares = self.getNonEmptySquares()
        if len(nonEmptySquares) < 16: #board isn't full
            return False


        for i in range(4):
            for j in range(4):
                try:
                    if self.board[i][j] == self.board[i][j+1] or self.board[i][j] == self.board[i+1][j]:
                        return False
                    
                except IndexError:
                    continue
        return True
            
    
'''
printBoard(board)
while True:
    x=input()
    move(board, x)
    board = newNumber(board)
    printBoard(board)
    

'''



        
