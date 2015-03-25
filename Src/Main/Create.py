import Main
from Main import LevelCompletion

def text(text, text_x, text_y, size):
    TextFont = Main.pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, TextFont)
    TextRect.center = ((text_x),(text_y))
    Main.screen.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, Main.Black)
    return textSurface, textSurface.get_rect()


def button(msg, button_x, button_y, button_w, button_h, icolour, acolour, fontsize, action= None): # icolour = inactive colour & acolour = active colour
    global nresets
    global current_level

    pos = Main.pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    click = Main.pygame.mouse.get_pressed()
    
    
    #Buttons:
    if button_x+button_w > mouse_x > button_x and button_y+button_h > mouse_y > button_y:
        Main.pygame.draw.rect(Main.screen, acolour, (button_x,button_y,button_w,button_h))
        if click[0] == 1 and action!= None:
            if action == "level 1":
                Main.game_level("level 1", "level 2", "reset_level1", 2, 2, 4, 4, 5, 4, 3, 5, 3, 3, 1, 4, 5, 0, 3, 4, 1, 2, 5, 3, 5, 0, 3, 4, 2, 2, 4, 4, 1, 2, 5, 3, 3, 3, 1, 4, 5, 4, 3, 5, 6, 28, 15, 29, 14, 24, 22, 26, 30, 34)
            
            elif action == "instructions":
                Main.instruction_menu()
                
            elif action == "quit":
                Main.pygame.quit()
                quit()
                
            elif action == "main menu":
                Main.game_intro()
                
            elif action == "reset_level1":
                if Main.nresets == -1:
                    reset_font = Main.pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Main.Red)
                    Main.screen.blit(reset_text,(5,620))
                else:
                    Main.game_level("level 1", "level 2", "reset_level1", 2, 2, 4, 4, 5, 4, 3, 5, 3, 3, 1, 4, 5, 0, 3, 4, 1, 2, 5, 3, 5, 0, 3, 4, 2, 2, 4, 4, 1, 2, 5, 3, 3, 3, 1, 4, 5, 4, 3, 5, 6, 28, 15, 29, 14, 24, 22, 26, 30, 34)

                    
            elif action == "reset_level2":
                if Main.nresets == -1:
                    reset_font = Main.pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Main.Red)
                    Main.screen.blit(reset_text,(5,620))
                else:
                    Main.game_level("level 2", "level 3", "reset_level2", 0, 1, 5, 3, 1, 1, 5, 4, 3, 1, 4, 4, 1, 3, 0, 5, 1, 2, 1, 4, 1, 3, 0, 5, 0, 1, 5, 3, 1, 2, 1, 4, 3, 1, 4, 4, 1, 1, 5, 4, 20, 31, 7, 24, 14, 26, 10, 29, 8, 30)
            
            elif action == "reset_level3":
                if Main.nresets == -1:
                    reset_font = Main.pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Main.Red)
                    Main.screen.blit(reset_text,(5,620))
                else:
                    Main.game_level("level 3", "level 4", "reset_level3", 4, 1, 4, 4, 4, 2, 4, 5, 5, 1, 3, 5, 0, 0, 1, 4, 0, 1, 2, 5, 0, 0, 1, 4, 4, 1, 4, 4, 0, 1, 1, 4, 5, 1, 3, 5, 4, 2, 4, 5, 1, 26, 11, 29, 7, 33, 12, 34, 17, 35)
                    
            elif action == "reset_level4":
                if Main.nresets == -1:
                    reset_font = Main.pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Main.Red)
                    Main.screen.blit(reset_text,(5,620))
                else:
                    Main.game_level("level 4", "level 5", "reset_level4", 5, 0, 0, 4, 0, 0, 3, 4, 1, 2, 2, 3, 0, 2, 2, 4, 0, 1, 3, 3, 0, 2, 2, 4, 5, 0, 0, 4, 0, 1, 3, 3, 1, 2, 2, 3, 0, 0, 3, 4, 13, 27, 6, 25, 7, 22, 14, 21, 1, 28)

            elif action == "reset_level5":
                if Main.nresets == -1:
                    reset_font = Main.pygame.font.SysFont(None, 25)
                    reset_text = reset_font.render("No more resets available", True, Main.Red)
                    Main.screen.blit(reset_text,(5,620))
                else:
                    Main.game_level("level 5", "game complete", "reset_level5", 1, 2, 3, 2, 2, 4, 4, 4, 1, 1, 2, 5, 5, 0, 0, 5, 5, 1, 3, 5, 5, 0, 0, 5, 1, 2, 3, 2, 5, 1, 3, 5, 1, 1, 2, 5, 2, 4, 4, 4, 6, 31, 14, 16, 12, 34, 8, 33, 27, 29)

                
            elif action == "level 2":
                Main.game_level("level 2", "level 3", "reset_level2", 0, 1, 5, 3, 1, 1, 5, 4, 3, 1, 4, 4, 1, 3, 0, 5, 1, 2, 1, 4, 1, 3, 0, 5, 0, 1, 5, 3, 1, 2, 1, 4, 3, 1, 4, 4, 1, 1, 5, 4, 20, 31, 7, 24, 14, 26, 10, 29, 8, 30)

            elif action == "level 3":
                Main.game_level("level 3", "level 4", "reset_level3", 4, 1, 4, 4, 4, 2, 4, 5, 5, 1, 3, 5, 0, 0, 1, 4, 0, 1, 2, 5, 0, 0, 1, 4, 4, 1, 4, 4, 0, 1, 1, 4, 5, 1, 3, 5, 4, 2, 4, 5, 1, 26, 11, 29, 7, 33, 12, 34, 17, 35)
    
            elif action == "level 4":
                Main.game_level("level 4", "level 5", "reset_level4", 5, 0, 0, 4, 0, 0, 3, 4, 1, 2, 2, 3, 0, 2, 2, 4, 0, 1, 3, 3, 0, 2, 2, 4, 5, 0, 0, 4, 0, 1, 3, 3, 1, 2, 2, 3, 0, 0, 3, 4, 13, 27, 6, 25, 7, 22, 14, 21, 1, 28)
            
            elif action == "level 5":
                Main.game_level("level 5", "game complete", "reset_level5", 1, 2, 3, 2, 2, 4, 4, 4, 1, 1, 2, 5, 5, 0, 0, 5, 5, 1, 3, 5, 5, 0, 0, 5, 1, 2, 3, 2, 5, 1, 3, 5, 1, 1, 2, 5, 2, 4, 4, 4, 6, 31, 14, 16, 12, 34, 8, 33, 27, 29)

            elif action == "game complete":
                LevelCompletion.situation("game complete", action, current_level)
                Main.pygame.display.update()
                Main.time.sleep(1)
            
            elif action == "none":
                pass
                
                
    else:
        Main.pygame.draw.rect(Main.screen, icolour, (button_x,button_y,button_w,button_h))
    
    smallText = Main.pygame.font.Font("freesansbold.ttf", fontsize)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((button_x+(button_w/2),(button_y+(100/2))))
    Main.screen.blit(textSurf, textRect)