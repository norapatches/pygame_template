import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, x: int= 10, y: int= 40) -> None:
    '''Display a small debug surface with <info> on the screen at <x> and <y> positions'''
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

def debug_multiple(items: list, x: int= 10, y: int= 40) -> None:
    '''Display multiple debug surfaces with <items> on the screen at <x> and <y> positions'''
    display_surface = pygame.display.get_surface()
    for idx, item in enumerate(items):
        debug_surf = font.render(str(item), True, 'White')
        debug_rect = debug_surf.get_rect(topleft = (x, y + (idx * 30)))
        pygame.draw.rect(display_surface, 'Black', debug_rect)
        display_surface.blit(debug_surf, debug_rect)

def show_fps(clock: pygame.time.Clock, x= 10, y= 10) -> None:
    '''Display the current FPS on the topleft corner of the screen'''
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(f'FPS {clock.get_fps():.2f}', True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)