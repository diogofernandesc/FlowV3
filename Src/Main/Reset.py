import Main

def counter(nresets):
    '''
    Using variable nresets, blits the value of nresets each time it changes
    I had to have a condition for zero nresets otherwise the counter would not blit the last reset available as 0
    '''
    if Main.nresets >= 0:
        reset_font = Main.pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Resets available: "+str(nresets), True, Main.White)
        Main.screen.blit(reset_text,(5,605))
        
    else:
        reset_font = Main.pygame.font.SysFont(None, 25)
        reset_text = reset_font.render("Resets available: "+str(0), True, Main.White)
        Main.screen.blit(reset_text,(5,605))
