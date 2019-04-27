
# ----------------------------------------------------------------------
# I hereby certify that this program is solely the result
# of my own work and is in compliance with the Academic Integrity 
# policy of the course syllabus.
#
# I hope you enjoy playing this game as much as I enjoyed making it.
#
# - Deborah Hier
# ----------------------------------------------------------------------

import Draw
import random

Draw.setCanvasSize(805, 505)

# draw everything on the board (title, tiles, color palette, "moves")
def drawBoard(z):
    Draw.setBackground(Draw.BLACK)

    # color options
    palette = [Draw.RED, Draw.CYAN, Draw.MAGENTA, Draw.YELLOW, Draw.GREEN]

    # background pattern
    def diamond(x, y, width, height):
        coords = [x, y + height / 2, x + width / 2, y + height, x + width, \
                  y + height / 2, x + width / 2, y]
        Draw.polygon(coords)

    for i in range(0, 801, 80):
        for x in range(0, 501, 80):
            Draw.setColor(random.choice(palette))
            diamond(i, x, 10, 15)
            diamond(i + 30, x + 40, 20, 10)
            
    # border
    turq = Draw.color(10, 250, 210)
    Draw.setColor(turq)
    Draw.filledRect(0, 0, 8, 505)
    Draw.filledRect(0, 0, 805, 8)
    Draw.filledRect(798, 0, 8, 505)
    Draw.filledRect(0, 498, 805, 8)
    
    # title
    Draw.setColor(Draw.BLACK)
    Draw.filledRect(330, 20, 150, 50)
    Draw.setFontItalic(True)
    Draw.setFontSize(27)
    Draw.setColor(Draw.CYAN)
    Draw.string("F", 330, 20)
    Draw.setColor(Draw.MAGENTA)
    Draw.string("L", 350, 20)
    Draw.setColor(Draw.YELLOW)
    Draw.string("O", 370, 20)
    Draw.setColor(Draw.GREEN)
    Draw.string("O", 390, 20)
    Draw.setColor(Draw.RED)
    Draw.string("D", 410, 20)
    Draw.setColor(Draw.YELLOW)
    Draw.string("-", 430, 20)
    Draw.setColor(Draw.CYAN)
    Draw.string("I", 440, 20)
    Draw.setColor(Draw.MAGENTA)
    Draw.string("T", 450, 20)
    Draw.setColor(Draw.GREEN)
    
    Draw.setColor(Draw.WHITE)       # white border around tile grid 
    Draw.filledRect(295, 95, 310, 310)

    # draw tiles (15x15)
    for y in range(100, 381, 20):
        for x in range(300, 581, 20):
            box_color = random.choice(palette) # choose random color 
            Draw.setColor(box_color)           # for each tile
            Draw.filledRect(x, y, 20, 20)
            tiles.append(box_color)  # add color chosen to a list
    
    # draw color palette: (red, blue, purple, yellow, green)
    for i in range(len(palette)):
        Draw.setColor(palette[i])
        Draw.filledRect(150, z, 40, 40)
        Draw.setColor(Draw.WHITE)
        Draw.rect(150, z, 40, 40)
        z += 60

    Draw.setColor(Draw.BLACK)
    Draw.filledRect(30, 40, 40, 25)
    Draw.setColor(Draw.WHITE)
    Draw.setFontSize(20)
    Draw.string("Move:     ", 40, 40)

    # if the player has played 1 or more games, print the lowest amount
    # of turns that it has taken them to completely 'flood-it'
    if best_score < 1000:
        Draw.setColor(Draw.BLACK)
        Draw.filledRect(40, 440, 50, 45)
        Draw.setColor(Draw.WHITE)
        Draw.setFontSize(18)
        Draw.string("Best Score: " + str(best_score), 40, 450) 

    

# shows the player how many turns they have used so far
def turnCounter():

    Draw.setColor(Draw.BLACK)         # put a black rectangle over previous   
    Draw.filledRect(100, 30, 60, 40)  # turn so the turn counter can 
    Draw.setColor(Draw.WHITE)         # be cleared and updated
    
    Draw.setFontItalic(True)
    Draw.setFontBold(True)
    Draw.setFontSize(20)
    Draw.string(str(turn), 105, 40)


# returns True if all the colors are the same (AKA player won)
def win(colors):
    return all(x == colors[0] for x in colors)


# 'flood-fill algorithm':
def colorCheck(x, y, oldColor, newColor):

    # if the tile is not the oldColor or it is already the newColor, return 
    if colors_grid[x][y] != oldColor or colors_grid[x][y] == newColor:
        return

    # set the tile's color to the newColor
    colors_grid[x][y] = newColor

    # set color to newColor and draw a rectangle at the tile's (x,y) coords
    Draw.setColor(newColor)
    Draw.filledRect((y * 20) + 300, (x * 20) + 100, 20, 20) 

    # call the function on every possible neighboring tile 
    if x > 0:
        colorCheck(x - 1, y, oldColor, newColor)    # up
        
    if x < 14:
        colorCheck(x + 1, y, oldColor, newColor)    # down
        
    if y < 14:
        colorCheck(x, y + 1, oldColor, newColor)    # right
        
    if y > 0:
        colorCheck(x, y - 1, oldColor, newColor)    # left


# run the game 
def gameplay():
    while True:
    
        global turn
    
        #check if mouse was pressed and get coordinates 
        if Draw.mousePressed():
            newX = Draw.mouseX()
            newY = Draw.mouseY()
        
            # did the player click somewhere on the color palette?
            # if so, update color accordingly
            if newX >= 150 and newX <= 180:
                if (newY >= 120 and newY <= 160) \
                   or (newY >= 180 and newY <= 220) \
                   or (newY >= 240 and newY <= 280) \
                   or (newY >= 300 and newY <= 340) \
                   or (newY >= 360 and newY <= 400):
                
                    # was the red box clicked?
                    if newY >= 120 and newY <= 160:     color_chosen = Draw.RED
                    
                    # blue box?
                    elif newY >= 180 and newY <=220:    color_chosen = Draw.CYAN

                    # purple box?
                    elif newY >= 240 and newY <= 280:   color_chosen = Draw.MAGENTA                       
                
                    # yellow box?
                    elif newY >= 300 and newY <= 340:   color_chosen = Draw.YELLOW
                           
                    # green box?
                    elif newY >= 360 and newY <= 400:   color_chosen = Draw.GREEN           
            
                    turn += 1
                    turnCounter()
                    colorCheck(0, 0, colors_grid[0][0], color_chosen)
            
            # if the player won exit the loop
            if win(colors_grid):
                break 


# give player the option to play again or exit
def playAgain():

    global best_score
    
    # clear the baard and ask the player if they want to play again (Y or N)
    # if Y, start a new game. if N, thank them for playing and end loop
    Draw.clear()
    Draw.setColor(Draw.MAGENTA)
    Draw.string("Congratulations! You won.", 100, 200)
    Draw.string("Would you like to play again? Enter Y or N.", 200, 250)

    if best_score <= turn:
        Draw.string("Current Score: " + str(turn), 40, 400)
        Draw.string("Best: " + str(best_score), 40, 450)
    else:
        Draw.string("New peronsal best! You won in "  + str(turn) + " turns!", 40, 450)
                                    # if the player's current best score is
        best_score = turn           # greater than the amount of turns they used, 
                                    # update the player's best score                               

    while True:
        
        if Draw.hasNextKeyTyped():
            
            key = Draw.nextKeyTyped()
            
            if key == "y":
                playing = True                  
                Draw.clear()
                return
            
            elif key == "n":
                playing = False
                Draw.clear()                    
                Draw.setFontSize(30)            
                Draw.string("Thanks for playing!", 250, 200)
                
                Draw.show(1500)                 

                Draw._on_closing()      # close game window 
                return

            
turn = 0   # for turn counter
playing = True
best_score = 1000   # set to very large number at first to 
                    # ensure that it is set to the value 
                    # of 'turn' after the first game
                    

# main game loop -->                    # 1. Introduction
while playing:                          # 2. Clear board
                                        # 3. Draw board
    tiles = []                          # 4. Play game
    colors_grid = []                    # 5. Play again? (restart or exit loop)

    turn = 0
    
    # introduction                          
    Draw.setBackground(Draw.BLACK)
    Draw.setFontSize(30)
    Draw.setFontItalic(True)
    Draw.setFontBold(True)
    Draw.setColor(Draw.MAGENTA)
    Draw.string("Welcome to Flood-It!", 170, 200)
    Draw.string("Click anywhere to begin.", 300, 250)
    Draw.show(800)
    
    if Draw.mousePressed():
                               
        Draw.clear()           
                               
        drawBoard(120)          
                                                               
        # divides the list of random box_color's chosen into a 15x15 grid (2d array)
        # so that the color of each box can be easily accessed  
        colors_grid = [tiles[i:i+15] for i in range(0, len(tiles), 15)]

        gameplay()
        
        Draw.show(500)
        
        # give player the option to start a new game
        playAgain()
        
