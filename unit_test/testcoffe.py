import unittest
from PyQt5.QtWidgets import QApplication
from coffeshop import CoffeeShop, CoffeeShopApp
from PyQt5.QtCore import Qt


class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        # Create an instance of CoffeeShop with initial prices
        self.coffee_shop = CoffeeShop(5.0, 7.0)

    def test_order_coffee_only(self):
        # Test for coffee only
        total = self.coffee_shop.process_order(True, False)
        self.assertEqual(total, 5.0, "Total should be 5.00 when only coffee is ordered.")

    def test_order_sandwich_only(self):
        # Test for sandwich only
        total = self.coffee_shop.process_order(False, True)
        self.assertEqual(total, 7.0, "Total should be 7.00 when only a sandwich is ordered.")

    def test_order_both(self):
        # Test for both coffee and sandwich
        total = self.coffee_shop.process_order(True, True)
        self.assertEqual(total, 12.0, "Total should be 12.00 when both coffee and sandwich are ordered.")

    def test_order_none(self):
        # Test for no items ordered
        total = self.coffee_shop.process_order(False, False)
        self.assertEqual(total, 0.0, "Total should be 0.00 when no items are ordered.")


if __name__ == '__main__':
    app = QApplication([])  # Start the Qt application to run the test cases
    unittest.main()
