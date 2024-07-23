import pygame

class Example:
    def __init__(self, stateManager) -> None:
        self.display = pygame.display.get_surface()
        self.stateManager = stateManager
    
    def run(self, delta: float):
        self.display.fill('gray')

