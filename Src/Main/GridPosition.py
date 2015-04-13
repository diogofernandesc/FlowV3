import pygame

import Main


# Checks if user has clicked circle to give line_colour a value, at mouse click event
def no_linecolour_crash():
    if Main.line_colour == ():
        crash_font = pygame.font.SysFont(None, 25)
        crash_text = crash_font.render("Please click a circle to begin", True, Main.Red)
        Main.screen.blit(crash_text,(350,605))
    

def grid_moving_circle(gridn_x, gridn_y, cctr_x, cctr_y, gridn):
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    
    if Main.line_colour == ():
        # Stops the program from crashing when the variable line_colour is empty and an attempt to draw without click happens
        reset_font = pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Please click a circle to begin", True, Main.Red)
        Main.screen.blit(reset_text,(350,605))
        
    elif ((int(mouse_x/100) == gridn_x) and (int(mouse_y/100) == gridn_y)):
        # Draws circles as user moves mouse:
        pygame.draw.circle(Main.screen, Main.line_colour, (cctr_x, cctr_y), 30)
        '''This is used so that when the value of line_colour is occupied by a value given by the click of the user in the
        'line' module it turns to black
        This gives the impression to the user that since the warning has now gone that they can now draw
        The warning would be: Please click a circle to begin'''
        reset_font = pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Please click a circle to begin", True, Main.Black)
        Main.screen.blit(reset_text,(350,605))
    
    
    
def pst():
    
    '''
    Draws the smaller circles on the screen as the user enters that "box":
    - These calls to the grid_moving circle function tell the program where exactly to draw the circle if the user has the left mouse button clicked when in that position
    '''
    
    # First row:
    
    grid_moving_circle(0, 0, 50, 50, 1)
    grid_moving_circle(1, 0, 150, 50, 2)
    grid_moving_circle(2, 0, 250, 50, 3)
    grid_moving_circle(3, 0, 350, 50, 4)
    grid_moving_circle(4, 0, 450, 50, 5)
    grid_moving_circle(5, 0, 550, 50, 6)
    
    # Second row:
    
    grid_moving_circle(0, 1, 50, 150, 7)
    grid_moving_circle(1, 1, 150, 150, 8)
    grid_moving_circle(2, 1, 250, 150, 9)
    grid_moving_circle(3, 1, 350, 150, 10)
    grid_moving_circle(4, 1, 450, 150, 11)
    grid_moving_circle(5, 1, 550, 150, 12)
    
    # Third row:
    
    grid_moving_circle(0, 2, 50, 250, 13)
    grid_moving_circle(1, 2, 150, 250, 14)
    grid_moving_circle(2, 2, 250, 250, 15)
    grid_moving_circle(3, 2, 350, 250, 16)
    grid_moving_circle(4, 2, 450, 250, 17)
    grid_moving_circle(5, 2, 550, 250, 18)
    
    # Fourth row:
    
    grid_moving_circle(0, 3, 50, 350, 19)
    grid_moving_circle(1, 3, 150, 350, 20)
    grid_moving_circle(2, 3, 250, 350, 21)
    grid_moving_circle(3, 3, 350, 350, 22)
    grid_moving_circle(4, 3, 450, 350, 23)
    grid_moving_circle(5, 3, 550, 350, 24)
    
    # Fifth row:
    
    grid_moving_circle(0, 4, 50, 450, 25)
    grid_moving_circle(1, 4, 150, 450, 26)
    grid_moving_circle(2, 4, 250, 450, 27)
    grid_moving_circle(3, 4, 350, 450, 28)
    grid_moving_circle(4, 4, 450, 450, 29)
    grid_moving_circle(5, 4, 550, 450, 30)
    
    # Sixth row:
    
    grid_moving_circle(0, 5, 50, 550, 31)
    grid_moving_circle(1, 5, 150, 550, 32)
    grid_moving_circle(2, 5, 250, 550, 33)
    grid_moving_circle(3, 5, 350, 550, 34)
    grid_moving_circle(4, 5, 450, 550, 35)
    grid_moving_circle(5, 5, 550, 550, 36)
    
        
       
