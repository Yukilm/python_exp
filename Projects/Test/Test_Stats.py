import pytest
from Game_stats import GameStats
from Settings import Settings

class TestGameStats:
    @pytest.fixture
    def ai_game(self):
        settings = Settings()
        return AI_Game(settings)

    def test_reset_stats(self, ai_game):
        stats = GameStats(ai_game)  # 创建GameStats实例
        stats.score = 100  # 设置分数为100
        stats.ships_left = 2  # 设置飞船剩余数量为2
        stats.reset_stats()  # 调用reset_stats方法重置统计信息
        assert stats.score == 0  # 检查分数是否被重置为0
        assert stats.ships_left == ai_game.settings.ship_limit  # 检查飞船剩余数量是否被重置为初始值
        assert stats.high_score == 0  # 检查高分是否被重置为0
        assert stats.level == 1  # 检查等级是否被重置为1

class AI_Game:
    def __init__(self, settings):
        self.settings = settings

class Settings:
    def __init__(self):
        self.ship_limit = 3