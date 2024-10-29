
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
            return "#Circular"
        self._evaluating.add(cell)
        value = self.get(cell)
        if value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        elif value.startswith("="):
            result = self.evaluate_formula(value)
        else:
            try:
                result = int(value)
            except ValueError:
                result = "#Error"
        self._evaluating.remove(cell)
        return result

    def evaluate_formula(self, value: str) -> Union[int, str]:
        if value[1:].isdigit():
            return int(value[1:])
        if value[1:].startswith("'") and value[-1] == "'":
            return value[2:-1]
        referenced_cell = value[1:]
        return self.evaluate(referenced_cell)

