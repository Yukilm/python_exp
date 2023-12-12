import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings

        self.image = pygame.image.load('D:/Python/python_exp/Projects/Image/ship.bmp')
        self.rect = self.image.get_rect()

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            if self.moving_left:
                self.x -= self.setting.ship_speed
        if self.moving_up and self.rect.top > 0:
            if self.moving_up:
                self.y -= self.setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_down:
                self.y += self.setting.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)