class GameLogger:
    def __init__(self):
        self.fight_log = []
        self.event_log = []
        self.system_log = []

    def log(self, msg, log_type="fight"):
        if log_type == "fight":
            self.fight_log.append(msg)
        elif log_type == "event":
            self.event_log.append(msg)
        elif log_type == "system":
            self.system_log.append(msg)

    def get_log(self, log_type="fight"):
        if log_type == "fight":
            return "\n".join(self.fight_log)
        elif log_type == "event":
            return "\n".join(self.event_log)
        elif log_type == "system":
            return "\n".join(self.system_log)
        return ""

# Global logger
logger = GameLogger()