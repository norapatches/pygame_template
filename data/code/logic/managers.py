from time import time

class StateManager:
    def __init__(self, initial: str) -> None:
        self._state = initial
        self._previous_state = None
        self._running = True
    
    @property
    def state(self) -> str:
        return self._state
    
    @property
    def previous_state(self) -> str:
        return self._previous_state
    
    @property
    def running(self) -> bool:
        return self._running
    
    def set_state(self, new: str):
        self._previous_state = self.state
        self._state = new


class SoundManager:
    def __init__(self) -> None:
        pass


class TimeManager:
    def __init__(self) -> None:
        self._delta = 0
        self._current = 0
        self._previous = time()
    
    @property
    def delta(self) -> float:
        return self._delta
    
    @property
    def current(self) -> float:
        self._current = time()
        return self._current
    
    def run_clock(self) -> None:
        self._current = time()
        self._delta = self._current - self._previous
        self._previous = self._current