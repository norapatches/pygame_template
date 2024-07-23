from data.code.logic.managers import StateManager, SoundManager, TimeManager
from data.code.shared.settings import Settings
from data.code.states.example import Example
import pygame
from sys import exit

class Game:
    def __init__(self):
        '''Game setup'''
        pygame.init()
        pygame.display.set_caption('*caption*')
        
        self.display = pygame.display.set_mode(Settings.display_resolution)
        self.clock = pygame.time.Clock()
        
        self.stateManager = StateManager('example')
        self.soundManager = SoundManager()
        self.timeManager = TimeManager()
        
        self.example = Example(self.stateManager)
        
        self.states = {
            'example': self.example
        }
    
    def run(self):
        '''Game loop'''
        while self.stateManager.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Calculate delta time
            self.timeManager.run_clock()
            # Run state
            self.states[self.stateManager.state].run(self.timeManager.delta)
            # Update screen & limit fps
            pygame.display.update()
            self.clock.tick(Settings.fps)


if __name__ == "__main__":
    game = Game()
    game.run()