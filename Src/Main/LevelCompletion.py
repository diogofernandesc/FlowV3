import Main, Create

def situation(situation, nextlevel, current_level):
    done = False
    while not done:
        for event in Main.pygame.event.get():
            if event.type == Main.pygame.QUIT:
                done = True  # Closes the game and exits the loop
        
        Create.button("",20,170, 560, 150, Main.Lightblue, Main.Lightblue, 30, "none")
        Create.button("",20,380, 560, 150, Main.Lightblue, Main.Lightblue, 30, "none")
        
        if situation == "level complete":
            Main.nresets = 3
            # This will determine what will happen when the level is completed:
            # At this point a message comes up saying level complete after all have been linked
            text = Main.font.render("Level Complete", True, Main.Black)
            textpos = text.get_rect(centerx=Main.background.get_width()/2)
            textpos.top = 210
            Main.screen.blit(text, textpos)
            Create.button("Next level",50,400, 200, 100, Main.DarkGreen, Main.Green, 30, nextlevel)
            Create.button("Quit game",350,400, 200, 100, Main.DarkGrey, Main.Grey, 30, "quit")
            
        elif situation == "out of time":
            Main.nresets = 3
            text = Main.font.render("Out of time!", True, Main.Black)
            textpos = text.get_rect(centerx=Main.background.get_width()/2)
            textpos.top = 210
            Main.screen.blit(text, textpos)
            Create.button("Retry",50,400, 200, 100, Main.DarkGreen, Main.Green, 30, "level 1")
            Create.button("Quit game",350,400, 200, 100, Main.DarkGrey, Main.Grey, 30, "quit")
            
            
        elif situation == "game complete":
            text = Main.font.render("Game Complete!", True, Main.Black)
            textpos = text.get_rect(centerx=Main.background.get_width()/2)
            textpos.top = 210
            Main.screen.blit(text, textpos)
            Create.button("Main Menu",50,400, 200, 100, Main.DarkGreen, Main.Green, 30, "main menu")
            Create.button("Quit game",350,400, 200, 100, Main.DarkGrey, Main.Grey, 30, "quit")
            
        Main.pygame.display.flip()