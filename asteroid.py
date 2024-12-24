import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, radius=self.radius,width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = self.velocity.rotate(random.uniform(20,50)) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_postive = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid_postive.velocity = random_angle
            new_asteroid_negative = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid_negative.velocity = random_angle * -1