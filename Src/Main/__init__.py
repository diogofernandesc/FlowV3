# Defining colours for the circles, paths(lines) and grid background

import Main
import pygame
import pygame.time
import pygame.font
import pygame.gfxdraw
import time

from Main import Grid, CircleRender, GridPosition, Connection, CheckPosition, Create, Time, LevelCompletion, Reset, Line


Black = (0 , 0, 0)
White = (255, 255, 255)
Blue = (0 , 0, 255)
DarkBlue = (0, 0, 180)
Red = (255, 0, 0)
DarkRed = (200,0,0)
Yellow = (255, 255, 0)
DarkYellow = (225, 200, 0)
Orange = (255, 100, 0)
Green = (0, 255, 0)
DarkGreen = (0, 200, 0)
Lightblue = (50, 255, 200)
DarkLightblue = (50, 255, 170)
Grey = (150, 150, 150)
DarkGrey = (110, 110, 100)
VeryDarkGrey = (20, 20, 20)


# Initialize pygame imported modules
pygame.init()

display_width = 600
display_height = 800
scr_size = (display_width, display_height)
screen = pygame.display.set_mode(scr_size)

clock = pygame.time.Clock()

# Loops until the user clicks the close Button
done = False

# Font + background used to create the popup message when level is complete
font = pygame.font.Font(None, 100)
background = pygame.Surface(screen.get_size())

# Default value for line colour
line_colour = ()
    
# Default value for grid position
grid_position = ()

# Defining grid positions for circles
# Array storing different grid positions possible for circles (their center) for both x and y:


'''
Position in pixels: 
Position 0: 50
position 1: 150
position 2: 250 
position 3: 350 
position 4: 450
position 5: 550
'''

grid = [50, 150, 250, 350, 450, 550]


pygame.init()

'''
Rendering of circles on the screen:
Render method takes 3 arguments: x-coordinate for center, y-coordinate for center, colour (in that order)
This will allow me to change the position of the circles for each level
'''

# Amount of resets available to player
nresets = 3

# Condition variables for clicks
Orange1Clicked = False
Orange2Clicked = False
Red1Clicked = False
Red2Clicked = False
Yellow1Clicked = False
Yellow2Clicked = False
Green1Clicked = False
Green2Clicked = False
Blue1Clicked = False
Blue2Clicked = False

# Condition variables for links
OrangeLink = False
RedLink = False
YellowLink = False
GreenLink = False
BlueLink = False


                                

def instruction_menu():
    pygame.display.set_caption("Flow Instructions")
    instrMenu = True
    while instrMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill(Yellow)

        ''' Text procedure used to create list of instructions which take parameters for actual instruction,
        x-axis position, y-axis position and font size'''
        Create.text("Instructions", 300, 100, 70)
        Create.text("The objective of flow is to connect all the circle pairs of the same colour, together:",300,200,15)
        Create.text("- Click one of the circles to begin", 300, 250, 15)
        Create.text("- Hold down the left mouse button and drag to its colour partner to complete the link", 300, 300, 15)
        Create.text("- Once a link is complete, the link colour will light up at the bottom of the screen", 300, 350, 15)
        Create.text("- You have 15 seconds to complete the level", 300, 400, 15)
        Create.text("- You have three resets available to you, which also reset the time!", 300, 450, 15)
        Create.text("- Enjoy yourself!", 300,500, 15)
        Create.button("Play", 50,600,200,100, DarkGreen, Green,30, "level 1")
        Create.button("Quit",350,600,200,100, DarkRed, Red,30, "quit")
        
        pygame.display.update()


def game_intro():
    pygame.display.set_caption("Flow Main Menu")
    Gintro = True
    
    while Gintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        screen.fill(Yellow)
        largeText = pygame.font.Font('freesansbold.ttf', 150)
        TextSurf, TextRect = Create.text_objects("Flow", largeText)
        TextRect.center = ((display_width/2),(display_height*0.25))
        screen.blit(TextSurf, TextRect)
        
        Create.button("Play", 200,300,200,100, DarkGreen, Green,30, "level 1")
        Create.button("Instructions",200,450,200,100, DarkBlue, Blue, 30, "instructions")
        Create.button("Quit",200,600,200,100, DarkRed, Red, 30, "quit")
        
        
        pygame.display.update()
        

def game_level(current_level, action, rAction, R1x, R1y, R2x, R2y, B1x, B1y, B2x, B2y, G1x, G1y, 
                G2x, G2y, O1x, O1y, O2x, O2y, Y1x, Y1y, Y2x, Y2y,o_x1, o_y1, o_x2, o_y2, r_x1, r_y1, r_x2, r_y2, 
                yel_x1, yel_y1, yel_x2, yel_y2, g_x1, g_y1, g_x2, g_y2, b_x1, b_y1, b_x2, b_y2,
                orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2):
    '''
     Arguments: Big letters (R, B, G, Y, O) represent stationary circles, small letters (o, r, g, y, b) used to check connections complete or if clicked
     Arguments: action to say what happens after level complete, and rAction for action for the reset button
    '''
    global Orange1Clicked
    global Orange2Clicked 
    global Red1Clicked
    global Red2Clicked
    global Yellow1Clicked
    global Yellow2Clicked
    global Green1Clicked
    global Green2Clicked
    global Blue1Clicked
    global Blue2Clicked
    global OrangeLink
    global RedLink
    global YellowLink
    global GreenLink
    global BlueLink
    global mouse_x
    global mouse_y
    global nresets
    global line_colour
    global frame_count
    global frame_rate
    global level_time
    global grid_position
    
    # Naming the caption of the window opened for the Game
    pygame.display.set_caption("Flow " + current_level)
    
    
    frame_count = 0
    frame_rate = 60

    # Time for each level:
    level_time = 15
    
    # Fill Screen in black for background
    screen.fill(Black)
    
    circle_list = pygame.sprite.Group()

    # Red Circle Pair:
            
    RedCircle1 = CircleRender.grid_circle(grid[R1x], grid[R1y], Red)
    RedCircle2 = CircleRender.grid_circle(grid[R2x], grid[R2y], Red)
    RedCircle1.render()
    RedCircle2.render()
        
    # Blue Circle Pair:
            
    BlueCircle1 = CircleRender.grid_circle(grid[B1x], grid[B1y], Blue)
    BlueCircle2 = CircleRender.grid_circle(grid[B2x], grid[B2y], Blue)
    BlueCircle1.render()
    BlueCircle2.render()
            
    # Green Circle Pair:
            
    GreenCircle1 = CircleRender.grid_circle(grid[G1x], grid[G1y], Green)
    GreenCircle2 = CircleRender.grid_circle(grid[G2x], grid[G2y], Green)
    GreenCircle1.render()
    GreenCircle2.render()
            
    
    # Orange Circle Pair:
            
    OrangeCircle1 = CircleRender.grid_circle(grid[O1x], grid[O1y], Orange)
    OrangeCircle2 = CircleRender.grid_circle(grid[O2x], grid[O2y], Orange)
    OrangeCircle1.render()
    OrangeCircle2.render()
            
    # Yellow Circle Pair:
            
    YellowCircle1 = CircleRender.grid_circle(grid[Y1x], grid[Y1y], Yellow)
    YellowCircle2 = CircleRender.grid_circle(grid[Y2x], grid[Y2y], Yellow)
    YellowCircle1.render()
    YellowCircle2.render()
    
    
    # Sprite list with all the circles
    circle_list.add(RedCircle1, RedCircle2, BlueCircle1, BlueCircle2, GreenCircle1, GreenCircle2, OrangeCircle1, OrangeCircle2, YellowCircle1, YellowCircle2)
    
    
    # Grid built here:
    Grid.build_grid()

    Reset.counter(nresets)
    Connection.complete_status()
    
    '''# Default value for line colour
    line_colour = ()
    
    # Default value for grid position
    grid_position = ()'''
    
    
    # Condition variables for links
    OrangeLink = False
    RedLink = False
    YellowLink = False
    GreenLink = False
    BlueLink = False
    
    Red1Clicked = False
    Red2Clicked = False
    Orange1Clicked = False
    Orange2Clicked = False
    Yellow1Clicked = False
    Yellow2Clicked = False
    Green1Clicked = False
    Green2Clicked = False
    Blue1Clicked = False
    Blue2Clicked = False
    
    
    done = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Closes the game and exits the loop
                pygame.quit()
                quit()
                    
                    #carry this on to check condition to be checked later for allowing to mouse to draw anywhere.
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # This stops program from crashing if user clicks anywhere but not the actual circle because line_colour would have no value
                GridPosition.no_linecolour_crash()
                Line.linecolour(o_x1, o_y1, o_x2, o_y2, r_x1, r_y1, r_x2, r_y2, yel_x1, yel_y1, yel_x2, yel_y2, g_x1, g_y1, g_x2, g_y2, b_x1, b_y1, b_x2, b_y2)
                CheckPosition.pst()
                Connection.clicked(orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2)
                # Checks whether user clicks the reset button:
                if 50+200 > mouse_x > 50 and 650+100 > mouse_y > 650:
                    if nresets == -1:
                        Reset.counter(nresets)
                        
                    else:
                        nresets = nresets - 1
                        Reset.counter(nresets)
                
            elif event.type == pygame.MOUSEMOTION:
                state = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                        
                if state[0] == 1:
                    #Line.check() # Gets the line colour by checking the position of where the user clicks
                    GridPosition.pst()
                    #click_movement(mouse_x, mouse_y)
                    CheckPosition.pst()
    
                    Connection.isConnected(orangegp1, orangegp2, redgp1, redgp2, yellowgp1, yellowgp2, greengp1, greengp2, bluegp1, bluegp2)
                            
            if ((OrangeLink == True) and (RedLink == True) and (YellowLink == True) and (GreenLink == True) and (BlueLink == True)):
                # Wait for 1 second because there seems to be a problem whereby if the user is still holding the mouse the program will continue evaluating in other circumstances, explained in project:
                time.sleep(1)
                if current_level == "level 5":
                    # Bring up game complete window if the 5th level is complete:
                    LevelCompletion.situation("game complete", action, current_level)
                    
                else:
                    # Bring up level complete screen if the current level is complete
                    LevelCompletion.situation("level complete", action, current_level)
                    
                    
                
                
         
        # Countdown timer: 
        Time.timer("out of time", action, current_level)
        Create.button("Reset Paths", 25,640,150,100, DarkBlue, Blue, 20, rAction)                  
        Create.button("Main menu", 225,640,150,100, DarkGreen, Green, 20, "main menu")
        Create.button("Quit game", 425,640,150,100, DarkRed, Red, 20, "quit")                       
        # Update screen with changes
        pygame.display.flip()



game_intro()
    
# Quit game
pygame.quit()
