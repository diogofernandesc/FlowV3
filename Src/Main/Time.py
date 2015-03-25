import Main, Create
from Main import LevelCompletion

def timer(situation, nextlevel, current_level):
    
    '''
    At each frame seconds tick down at the same rate that a second ticks down
    '''
    
    global frame_count
    global frame_rate
    global level_time
    
    timer_font = Main.pygame.font.SysFont(None, 25)
    total_seconds = Main.level_time - (Main.frame_count // Main.frame_rate)
    
    if total_seconds < 0:
        # Statements executed when time runs out:
        total_seconds = 0
        LevelCompletion.situation(situation, nextlevel, current_level)
        
    else:
        # Need this to create a black background over the blitted text as to not overlap
        Create.button("", 210, 605, 135, 20, Main.Black, Main.Black, 10, "none") 
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
         
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
         
        # Use python string formatting to format in leading zeros
        time_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
         
        # Blit to the screen
        time_text = timer_font.render(str(time_string), True, Main.White)
        Main.screen.blit(time_text, (210,605))
    
        # Controls the rate of change of frames 
        Main.frame_count += 1
        
        # Control the second change of the timer to be equal to a second
        Main.clock.tick(Main.frame_rate)