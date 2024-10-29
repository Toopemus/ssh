
from typing import Union

class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> Union[int, str]:
        value = self.get(cell)
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        if value.startswith("="):
            if value[1:].startswith("'") and value[-1] == "'":
                return value[2:-1]
            else:
                return value[1:]
        try:
            int_value = int(value)
            return int_value
        except ValueError:
            return "#Error"

