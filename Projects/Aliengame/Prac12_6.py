import sys
import pygame
from pygame.sprite import Sprite


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_width))
        pygame.display.set_caption('12-6')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # 键盘与鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 向右移动
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 向左移动
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right >= 800:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = Settings()

        self.image = pygame.image.load('D:/Python/python_exp/Projects/Image/ship.bmp')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

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
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0, 0, self.setting.bullet_height, self.setting.bullet_width)
        self.rect.midright = ai_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.setting.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.ship_speed = 1.5


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()