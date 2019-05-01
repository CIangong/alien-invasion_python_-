import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        #初始化飞船，并设置飞船所在屏幕
        super(Ship, self).__init__()
        self.screen = screen

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #设置飞船的起始位置（屏幕底部中央）
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self,ai_settings):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx+=ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx-=ai_settings.ship_speed_factor
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
