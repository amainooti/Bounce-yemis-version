import pygame
from settings import *
from tile import Tile
from Bounce import Player

class Level:

    def __init__(self):
        self.display_surface =pygame.display.get_surface()

        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        self.setup_level()

    def setup_level(self):
        for row_index,row in enumerate(LEVEL_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE 
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x,y),[self.visible_sprites, self.collision_sprites])
                elif col == "P":
                    Player((x,y),[self.visible_sprites,self.active_sprites], self.collision_sprites)
    
    def run(self):
        self.active_sprites.update()
        self.visible_sprites.custom_draw()
        

class CameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface =pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

    def custom_draw(self):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image,offset_pos)

