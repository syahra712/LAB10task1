from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox

class CoffeeShop:
    def __init__(self, coffee_price, sandwich_price):
        self.coffee_price = coffee_price
        self.sandwich_price = sandwich_price

    def process_order(self, wants_coffee, wants_sandwich):
        total = 0
        if wants_coffee: total += self.coffee_price
        if wants_sandwich: total += self.sandwich_price
        return total


class CoffeeShopApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Coffee Shop')
        self.setGeometry(100, 100, 250, 200)

        self.coffee_shop = CoffeeShop(5.0, 7.0)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Enter name')
        self.name_input.move(50, 20)

        self.coffee_button = QPushButton("Coffee", self)
        self.coffee_button.setCheckable(True)
        self.coffee_button.move(50, 60)

        self.sandwich_button = QPushButton("Sandwich", self)
        self.sandwich_button.setCheckable(True)
        self.sandwich_button.move(50, 100)

        self.order_button = QPushButton('Place Order', self)
        self.order_button.clicked.connect(self.place_order)
        self.order_button.move(50, 140)

    def place_order(self):
        name = self.name_input.text()
        coffee = self.coffee_button.isChecked()
        sandwich = self.sandwich_button.isChecked()

        if not name:
            QMessageBox.warning(self, 'Error', 'Please enter your name.')
            return

        total = self.coffee_shop.process_order(coffee, sandwich)
        if total == 0:
            QMessageBox.warning(self, 'Error', 'Select at least one item.')
        else:
            QMessageBox.information(self, 'Order Summary', f'Total: ${total:.2f}')


if __name__ == '__main__':
    app = QApplication([])
    window = CoffeeShopApp()
    window.show()
    app.exec_()
