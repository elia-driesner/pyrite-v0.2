import pygame

def cut_rect(image):
    image = image
    rect = image.get_rect()
    size = (rect.w, rect.h)
    surf = pygame.Surface(size)
    
    for row in range(0, size[1]):
        row_surf = pygame.Surface((size[0], 1))
        row_surf.set_colorkey((0,0,0))
        row_surf.blit(image, (0, 0), (0, row, size[0], 1))
        row_mask = pygame.mask.from_surface(row_surf)
        row_pixels = row_mask.count()
        print(row_pixels)
    
    for col in range(0, size[0]):
        col_surf = pygame.Surface((1, size[1]))
        col_surf.set_colorkey((0,0,0))
        col_surf.blit(image, (0, 0), (0, col, 1, size[1]))
        col_mask = pygame.mask.from_surface(col_surf)
        col_pixels = col_mask.count()
        print(col_pixels)
        
        