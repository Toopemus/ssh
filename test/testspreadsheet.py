from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_int(self):
        sheet = SpreadSheet()
        sheet.set("A1", "1")
        value = sheet.evaluate("A1")
        self.assertEqual(1, value)
