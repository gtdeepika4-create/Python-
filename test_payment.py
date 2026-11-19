import unittest
from decimal import Decimal
from task09_calculator_tests import payment

class PaymentTests(unittest.TestCase):
    def test_reference_payment(self):
        self.assertEqual(payment(10, 3.5, 8.5), Decimal("300.00"))
    def test_high_fat_snf(self):
        self.assertEqual(payment(10, 4.0, 9.0), Decimal("335.00"))
    def test_low_values(self):
        self.assertEqual(payment(5, 3.0, 7.5), Decimal("125.00"))
    def test_fat_boundaries(self):
        self.assertEqual(payment(1, 2.0, 8.5), Decimal("24.00"))
        self.assertEqual(payment(1, 7.0, 8.5), Decimal("44.00"))
    def test_invalid_litres(self):
        with self.assertRaises(ValueError):
            payment(-1, 3.5, 8.5)
    def test_invalid_fat(self):
        with self.assertRaises(ValueError):
            payment(1, 1.9, 8.5)
        with self.assertRaises(ValueError):
            payment(1, 7.1, 8.5)
    def test_invalid_snf(self):
        with self.assertRaises(ValueError):
            payment(1, 3.5, 0)

if __name__ == "__main__":
    unittest.main()
