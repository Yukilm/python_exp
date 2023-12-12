class Settings:
    """设置"""

    def __init__(self):
        """初始化设置"""
        self.aline_points = None
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.alien_points = 50

        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 子弹数量限制
        # self.bullets_allowed = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # 飞船速度
        self.ship_speed = 1.5
        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.aline_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)