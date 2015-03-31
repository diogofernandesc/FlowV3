import pygame
import pygame.gfxdraw

import Main




class grid_circle(pygame.sprite.Sprite):
    # Stationary circles class you need a pair of each colour
    def __init__(self, ctr_x, ctr_y, colour):
        # Takes the argument given as the actual values for the circle object to be created
        pygame.sprite.Sprite.__init__(self)
        self.ctr_x = ctr_x
        self.ctr_y = ctr_y
        self.radius = 40
        self.colour = colour
            
    def render(self):
        pygame.gfxdraw.filled_circle(Main.screen, self.ctr_x, self.ctr_y, self.radius, self.colour)

            

