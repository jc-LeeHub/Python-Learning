import pygame
from pygame.sprite import Sprite

#子弹类
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        #
        super(Bullet, self).__init__()
        self.screen = screen

        # 先创建一个矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        # 设置矩形位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    #子弹移动
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
