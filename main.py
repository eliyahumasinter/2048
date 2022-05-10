from backend import Game
import pygame


pygame.init()
WIDTH = 400
HEIGHT = 400
BG_COLOR = (100,50,255)
BLACK = (0,0,0)
RED = (255,0,0)
NUM_COLORS = {2:(128, 128, 128),
              4:(89, 108, 166),
              8:(172, 128, 83),
              16:(0, 255, 255),
              32:(64, 191, 64)	,
              64:(153, 77, 179)}

NUM_COLORS = {2:(255, 153, 153)	,
              4:(255, 204, 153),
              8:(255, 255, 153),
              16:(204, 255, 153),
              32:(153, 255, 153),
              64:(153, 255, 204),
              128:(153, 255, 255),
              256: (153, 230, 255),
              512:(153, 179, 255),
              1024:(179, 153, 255),
              2048:(230, 153, 255)
              }

screen = pygame.display.set_mode((WIDTH, HEIGHT))
scoreColor = BLACK


def grid():
    for i in range(1,6):
        pygame.draw.line(screen, BLACK, (50+(i*50),100), (50+(i*50),300), 2)
        pygame.draw.line(screen, BLACK, (100,50+(i*50)), (300,50+(i*50)), 2)
def writeText(string, coordx, coordy, fontSize, color):
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    text = font.render(string, True, color)
    textRect = text.get_rect()
    #set the position of the text
    textRect.center = (coordx, coordy)
    #add text to window
    screen.blit(text, textRect)

def drawSquare(number, color, position):
    y = position[0]*50+100
    x = position[1]*50 + 100
    pygame.draw.rect(screen, color, pygame.Rect(x+2,y+2,48,48))
    size = 30
    if int(number) >= 100:
        size = 25
    if int(number) >= 1000:
        size = 20
        
    writeText(str(number), x+25,y+25,size, BLACK)
    
def drawBoard(board):
    squaresToDraw = g.getNonEmptySquares()
    for square in squaresToDraw:
        number = board[square[0]][square[1]]
        drawSquare(number, NUM_COLORS[number], [square[0], square[1]])



g = Game()
run = True
while run:
    screen.fill((BG_COLOR))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                g.move("r")
            elif event.key == pygame.K_LEFT:
                g.move("l")
            elif event.key == pygame.K_UP:
                g.move("u")
            elif event.key == pygame.K_DOWN:
                g.move("d")
            elif event.key == pygame.K_RETURN:
                if g.gameOver == True:
                    g=Game()
            g.gameOver = g.checkGameOver()
  
    
    grid()
    writeText("2048", WIDTH/2, 50, 40, BLACK)
    drawBoard(g.board)
    if g.gameOver:
        writeText(f"Game Over: Score: {g.score}", WIDTH/2, 350, 33, RED)
        writeText("Press Enter to begin", WIDTH/2, 380, 22, BLACK)
    else:     
        writeText(f"Score: {g.score}", WIDTH/2, 350, 40, BLACK)
    pygame.display.flip()
