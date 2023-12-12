import random
import sys

import pygame
from random import randint
from pygame.sprite import Sprite


class Screen:
    def __init__(self):
        pygame.init()

        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_width))
        pygame.display.set_caption('13-2')

        self.stars = pygame.sprite.Group()

        self._create_star()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

    def _create_star(self):
        star = Star(self)

        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height

        self.available_x = self.screen.get_rect().width - (2 * star_width)
        number_stars_x = self.available_x // star_width + 1

        self.available_y = self.screen.get_rect().height - (2 * star_height)
        number_rows = self.available_y // star_height + 1

        List_X = []
        List_Y = []

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                List_X.append(current_x + star_width)
                List_X.append(current_x - star_width)
                List_Y.append(current_y + star_height)
                List_Y.append(current_y - star_height)

                # print(List_X)
                # print(List_Y)

                random_x = randint(0, self.available_x)
                random_y = randint(0, self.available_y)
                # self.setting.screen_width - star_width
                # self.setting.screen_height - star_height
                while current_x - star_width <= random_x <= current_x + star_width \
                        and current_y - star_height <= random_y <= current_y + star_height \
                            and random_x not in List_X and random_y not in List_Y:
                    random_x = randint(0, self.available_x)
                    random_y = randint(0, self.available_y)
                    # print('xxx')

                # print(random_x)
                # print(random_y)
                # print()

                current_x = random_x
                current_y = random_y

                self._create_stars(current_x, current_y)

    def _create_stars(self, x_position, y_position):
        new_star = Star(self)

        # new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position

        # new_star.rect.x = randint(0, self.available_x)
        # new_star.rect.y = randint(0, self.available_y)

        self.stars.add(new_star)


class Star(Sprite):
    def __init__(self, screens):
        super().__init__()
        self.screen = screens.screen

        self.image = pygame.image.load('D:/Python/python_exp/Projects/Image/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)


a = Screen()
a.run_game()