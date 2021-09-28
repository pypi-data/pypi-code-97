from enum import Enum


class TestResponseTaskStatus(str, Enum):
    PENDING = "pending"
    STARTING = "starting"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)