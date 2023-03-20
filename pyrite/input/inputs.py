import pygame
import sys

class Input:
    def __init__(self, game, config):
        self.config = config
        self.game = game
        self.mouse_state = {'left': False, 'left_hold': False, 'left_release': False, 
                            'right': False, 'right_hold': False, 'right_release': False,
                            'scroll_up': False, 'scroll_down': False}
        
        self.key_presses = []
        
        self.mouse_pos = (0, 0)
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.run = False
                pygame.quit()
                sys.exit(0)
            self.update(event)
        print(self.key_presses, self.mouse_pos, self.mouse_state)
        
    def reset(self):
        self.key_presses = []
        self.mouse_state = {'left': False, 'left_hold': False, 'left_release': False, 
                            'right': False, 'right_hold': False, 'right_release': False, 
                            'scroll_up': False, 'scroll_down': False}
        
    def update(self, event):
        self.mouse_pos = pygame.mouse.get_pos()
        self.reset()
        
        if event.type == pygame.KEYDOWN:
            if event.key in self.config['keybinds']:
                self.key_presses.append(event.key)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_state['left'] = True
                self.mouse_state['left_hold'] = True
            if event.button == 3:
                self.mouse_state['right'] = True
                self.mouse_state['right_hold'] = True
            if event.button == 4:
                self.mouse_state['scroll_up'] = True
            if event.button == 5:
                self.mouse_state['scroll_down'] = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_state['left_release'] = True
                self.mouse_state['left_hold'] = False
            if event.button == 3:
                self.mouse_state['right_release'] = True
                self.mouse_state['right_hold'] = False