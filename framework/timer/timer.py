from collections.abc import Callable, Iterable, Mapping
from threading import Timer as T
from typing import Any
from .timermanager import TimerManager as TM


class OneShotTimer:
    def __init__(self, interval: float, function: Callable | None = None, args: Iterable[Any] | None = None,
                 kwargs: Mapping[str, Any] | None = None) -> None:
        self.running = False
        self.interval = interval
        self.function = function
        if self.function is None:
            self.function = self.nonefunction
        self.args = args
        self.kwargs = kwargs
        self.timer = self.createTimer()

    def nonefunction(self):
        pass

    def setInterval(self, value):
        self.interval = value

    def createTimer(self):
        return OneShotBase(self.interval, self.function, self.args, self.kwargs, cleanupFuntion=self.cleanup)

    def startTimer(self):
        if self.running:
            return

        self.timer = self.createTimer()

        TM.activeTimers.append(self)

        self.timer.start()
        self.running = True

    def cleanup(self):
        if not self.running:
            return
        self.timer.cancel()
        TM.activeTimers.remove(self)
        self.running = False

    def stopTimer(self):
        self.cleanup()

class OneShotBase(T):
    def __init__(self, interval: float, function: Callable[..., object] | None = None,
                 args: Iterable[Any] | None = None, kwargs: Mapping[str, Any] | None = None,
                 cleanupFuntion: callable = None) -> None:
        super().__init__(interval, function, args, kwargs)
        self.cleanupFunciton = cleanupFuntion

    def run(self) -> None:
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.cleanupFunciton()
        self.finished.set()


class RepeatBase(OneShotBase):
    def __init__(self, interval: float, function: Callable[..., object] | None = None,
                 args: Iterable[Any] | None = None, kwargs: Mapping[str, Any] | None = None,
                 cleanupFuntion: callable = None) -> None:
        super().__init__(interval, function, args, kwargs, cleanupFuntion)

    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        self.cleanupFunciton()


class RepeatTimer(OneShotTimer):
    def __init__(self, interval: float, function: Callable[..., object] | None = None,
                 args: Iterable[Any] | None = None, kwargs: Mapping[str, Any] | None = None) -> None:
        super().__init__(interval, function, args, kwargs)

    def createTimer(self):
        return RepeatBase(self.interval, self.function, self.args, self.kwargs, cleanupFuntion=self.cleanup)
