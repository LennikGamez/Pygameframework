
class TimerManager:
    activeTimers = []

    @staticmethod
    def stopTimers():
        for timer in TimerManager.activeTimers:
            timer.cleanup()