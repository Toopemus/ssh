
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
        if cell in self._evaluating:
            return "#Error"
        self._evaluating.add(cell)
        value = self.get(cell)
        if value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        elif value.startswith("="):
            if value[1:].isdigit():
                result = int(value[1:])
            elif value[1:].startswith("'") and value[-1] == "'":
                result = value[2:-1]
            else:
                referenced_cell = value[1:]
                result = self.evaluate(referenced_cell)
        else:
            try:
                result = int(value)
            except ValueError:
                result = "#Error"
        self._evaluating.remove(cell)
        return result

