import pygame

class Camera(pygame.sprite.Group):
    BORDERS = {'left': 20, 'right': 20, 'top': 10, 'bottom': 10}
    '''The camera module. It has various modes to select from and a custom draw method'''
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        
        # BACKGROUND SURFACE & RECT
        
        # CAMERA OFFSET
        self.offset = pygame.math.Vector2()
        self.half_w = self.display.get_width() / 2
        self.half_h = self.display.get_height() / 2
        
        # BOX SETUP
        l = Camera.BORDERS['left']
        t = Camera.BORDERS['top']
        w = self.display.get_width() - (Camera.BORDERS['left'] + Camera.BORDERS['right'])
        h = self.display.get_height() - (Camera.BORDERS['top'] + Camera.BORDERS['bottom'])
        self.camera_rect = pygame.Rect(l, t, w, h)
    
    def center_target_camera(self, target):
        '''A camera that always follows the target'''
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def box_target_camera(self, target):
        '''A camera box that moves if target reaches the box bounds'''
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom
        
        self.offset.x = self.camera_rect.left - Camera.BORDERS['left']
        self.offset.y = self.camera_rect.top - Camera.BORDERS['top']
    
    
    def draw_ysorted(self, target):
        self.center_target_camera(target)
        self.box_target_camera(target)
        # DRAW BACKGROUND WITH OFFSET
        # DRAW ALL SPRITES WITH OFFSET
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_position)
    
    def draw_custom(self, target):
        self.center_target_camera(target)
        self.box_target_camera(target)
        # DRAW BACKGROUND WITH OFFSET
        # DRAW ALL SPRITES WITH OFFSET
        for sprite in self.sprites():
            offset_position = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_position)

