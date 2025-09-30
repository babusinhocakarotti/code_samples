class Counter:
    def __init__(self, start: int = 0):
        self._value = start

    def increment(self, step: int = 1) -> None:
        self._value += step

    def decrement(self, step: int = 1) -> None:
        self._value -= step

    def reset(self) -> None:
        self._value = 0

    def value(self) -> int:
        return self._value