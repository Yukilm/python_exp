import pygame
from Alien import Alien


# 创建一个虚拟的ai_game实例，可以使用Mock等方式
class MockSettings:
    alien_speed = 1
    fleet_direction = 1


class MockScreen:
    def get_rect(self):
        return pygame.Rect(0, 0, 800, 600)


class MockAiGame:
    def __init__(self):
        self.screen = MockScreen()
        self.settings = MockSettings()


def test_alien_update():
    ai_game = MockAiGame()
    alien = Alien(ai_game)

    alien.update()
    assert alien.rect.x == 61  # 验证横向移动是否符合预期


def test_alien_check_edges():
    ai_game = MockAiGame()
    alien = Alien(ai_game)

    screen_rect = alien.screen.get_rect()
    alien.rect.x = screen_rect.right - 1
    assert alien.check_edges() == True  # 验证边缘检查是否符合预期

    alien.rect.x = 0
    assert alien.check_edges() == True  # 验证边缘检查是否符合预期

    alien.rect.x = 10
    assert alien.check_edges() == False  # 验证边缘检查是否符合预期