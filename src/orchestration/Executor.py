from typing import List, Callable, Any

class Executor:

    def __init__(self) -> None:
        self.arr: List[Any] = []

    def add(self, fn: Callable):
        self.arr.append(fn)
    
    def add_parallel(self, func: Callable):
        if isinstance(self.arr[- 1], list):
            parallel = self.arr[- 1]
            parallel.append(func)
        else:
            parallel = [func]
            self.arr.append(parallel)

    def run(self):
        for x in range(0, len(self.arr)):
            
    
