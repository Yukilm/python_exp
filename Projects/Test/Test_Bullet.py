import pygame
from Bullet import Bullet


def test_bullet_update():
    ai_game = MockAiGame()  # 这里需要自行实现一个 MockAiGame 类
    bullet = Bullet(ai_game)
    bullet.update()
    assert bullet.rect.y == bullet.y


class MockAiGame:
    def __init__(self):
        self.screen = pygame.Surface((800, 600))
        self.settings = MockSettings()
        self.ship = MockShip()


class MockSettings:
    def __init__(self):
        self.bullet_color = (255, 255, 255)  # 设置合适的颜色
        self.bullet_width = 5  # 设置合适的宽度
        self.bullet_height = 10  # 设置合适的高度
        self.bullet_speed = 2  # 设置合适的速度


class MockShip:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 10, 10)  # 设置合适的坐标

    @property
    def midtop(self):
        return self.rect.midtop