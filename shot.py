from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, radius=SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt