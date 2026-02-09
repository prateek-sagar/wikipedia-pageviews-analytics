from typing import Callable, List, Any

class TaskNode:
    name: str
    function: Callable
    dependencies: List[str]
    stage: str
    consumes: Any
    produces: Any