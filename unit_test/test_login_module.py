import unittest
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox
from unittest.mock import patch

class TestLoginModule(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.username_input = QLineEdit(self.window)
        self.password_input = QLineEdit(self.window)
        self.login_button = QPushButton("Login", self.window)
        self.login_button.clicked.connect(self.validate_login)

    def validate_login(self):
        username, password = self.username_input.text(), self.password_input.text()
        if not username and not password:
            QMessageBox.critical(self.window, "Error", "Both fields are empty")
        elif username != "admin" and password != "password":
            QMessageBox.critical(self.window, "Error", "Both fields are filled incorrectly")
        elif not username or not password:
            QMessageBox.critical(self.window, "Error", "One of the fields is empty")
        elif username == "admin" and password == "password":
            QMessageBox.information(self.window, "Success", "Login successful")
        else:
            QMessageBox.critical(self.window, "Error", "One of the fields is filled correctly")

    def simulate_click(self, username, password, expected_msg, msg_type):
        self.username_input.setText(username)
        self.password_input.setText(password)
        with patch(f'PyQt5.QtWidgets.QMessageBox.{msg_type}') as mock_msg:
            self.login_button.click()
            mock_msg.assert_called_with(self.window, *expected_msg)

    def test_cases(self):
        cases = [
            ("", "", ("Error", "Both fields are empty"), "critical"),
            ("wrong", "wrong", ("Error", "Both fields are filled incorrectly"), "critical"),
            ("", "password", ("Error", "One of the fields is empty"), "critical"),
            ("admin", "password", ("Success", "Login successful"), "information"),
            ("admin", "wrong", ("Error", "One of the fields is filled correctly"), "critical"),
            ("wrong", "password", ("Error", "One of the fields is filled correctly"), "critical")
        ]
        for username, password, msg, msg_type in cases:
            self.simulate_click(username, password, msg, msg_type)

if __name__ == "__main__":
    unittest.main()
