from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_int(self):
        sheet = SpreadSheet()
        sheet.set("A1", "1")
        value = sheet.evaluate("A1")
        self.assertEqual(1, value)

    def test_evaluate_non_valid_int(self):
        sheet = SpreadSheet()
        sheet.set("A1", "1.5")
        value = sheet.evaluate("A1")
        self.assertEqual("#Error", value)

    def test_evaluate_valid_string(self):
        sheet = SpreadSheet()
        sheet.set("A1", "'Apple'")
        value = sheet.evaluate("A1")
        self.assertEqual("Apple", value)

    def test_evaluate_non_valid_string(self):
        sheet = SpreadSheet()
        sheet.set("A1", "Apple")
        value = sheet.evaluate("A1")
        self.assertEqual("#Error", value)

    def test_evaluate_formula_with_string(self):
        sheet = SpreadSheet()
        sheet.set("A1", "='Apple'")
        value = sheet.evaluate("A1")
        self.assertEqual("Apple", value)

    def test_evaluate_formula_with_int(self):
        sheet = SpreadSheet()
        sheet.set("A1", "=1")
        value = sheet.evaluate("A1")
        self.assertEqual(1, value)

    def test_evaluate_formula_with_non_valid_string(self):
        sheet = SpreadSheet()
        sheet.set("A1", "='Apple")
        value = sheet.evaluate("A1")
        self.assertEqual("#Error", value)

    def test_evaluate_formula_with_reference_valid_int(self):
        sheet = SpreadSheet()
        sheet.set("A1", "=B1")
        sheet.set("B1", "=42")
        value = sheet.evaluate("A1")
        self.assertEqual(42, value)

    def test_evaluate_formula_with_reference_non_valid_int(self):
        sheet = SpreadSheet()
        sheet.set("A1", "=B1")
        sheet.set("B1", "=42.5")
        value = sheet.evaluate("A1")
        self.assertEqual("#Error", value)

    def test_evaluate_formula_with_circular_reference(self):
        sheet = SpreadSheet()
        sheet.set("A1", "=B1")
        sheet.set("B1", "=A1")
        value = sheet.evaluate("A1")
        self.assertEqual("#Circular", value)