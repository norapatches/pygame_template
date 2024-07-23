from time import time

class Timer:
    '''A countdown timer using the time.time() function'''
    def __init__(self, duration, func = None, repeat = False) -> None:
        '''A new Timer instance. It needs the <duration> in seconds, it can call a <func> and it can <repeat> itself'''
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False
        self.repeat = repeat
    
    def activate(self) -> None:
        '''Start the timer object'''
        self.active = True
        self.start_time = time()
    
    def deactivate(self) -> None:
        '''Stop the timer object'''
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()
    
    def update(self) -> None:
        '''The timer update method to be called each frame'''
        current_time = time()
        if current_time - self.start_time >= self.duration:
            if self.func and self.start_time != 0:
                self.func()
            self.deactivate()

