from pathlib import Path


class GameStats:
    """ 跟踪游戏的统计信息 """

    def __init__(self, ai_game):
        """ 初始化统计信息 """
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 读取历史最高得分初始化历史最高得分
        filename = 'score.txt'
        path = Path(filename)
        high_score = path.read_text()
        high_score = high_score.rstrip()
        for score in high_score:
            self.highscore = int(score)

        self.high_score = self.highscore

    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


def update_score(self):
    """ 更新最高得分 """
    filename = 'score.txt'
    highscore = self.stats.high_score
    path = Path(filename)
    high_score = path.read_text()
    high_score = high_score.rstrip()
    for score in high_score:
        self.highscore = int(score)
    if highscore > self.highestscore:
        path.write_text(str(highscore))
        self.highscore = highscore