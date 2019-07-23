import pygame
from pygame.sprite import Sprite

#外星人类
class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像与外接矩阵
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #起始位置为屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    #检测外星人是否到达边缘
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    #向右移动外星人
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    #绘制外星人
    def blitme(self):
        self.screen.blit(self.image, self.rect)
