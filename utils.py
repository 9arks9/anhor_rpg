class GameLogger:
    def __init__(self):
        self.fight_log = []
        self.level_log = []
        self.enemy_log = []

    def log(self, msg, log_type="fight"):
        if log_type == "fight":
            self.fight_log.append(msg)
        elif log_type == "l":
            self.level_log.append(msg)
        elif log_type == "e":
            self.enemy_log.append(msg)

    def get_log(self, log_type="fight"):
        if log_type == "fight":
            return "\n".join(self.fight_log)
        elif log_type == "l":
            return "\n".join(self.level_log)
        elif log_type == "e":
            return "\n".join(self.enemy_log)
        return ""

# Global logger
logger = GameLogger()