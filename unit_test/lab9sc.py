import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Module")
        self.resize(300, 200)

        # Create layout
        layout = QVBoxLayout()

        # Username label and entry
        self.label_username = QLabel("Username:")
        layout.addWidget(self.label_username)
        self.entry_username = QLineEdit()
        layout.addWidget(self.entry_username)

        # Password label and entry
        self.label_password = QLabel("Password:")
        layout.addWidget(self.label_password)
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.entry_password)

        # Login button
        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.validate_login)
        layout.addWidget(self.btn_login)

        # Set layout and show window
        self.setLayout(layout)

    def validate_login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        # Check if both fields are empty
        if not username and not password:
            QMessageBox.critical(self, "Error", "Both fields are empty")

        # Check if both fields are filled incorrectly
        elif username != "admin" and password != "password":
            QMessageBox.critical(self, "Error", "Both fields are filled incorrectly")

        # Check if one of the fields is empty
        elif not username or not password:
            QMessageBox.critical(self, "Error", "One of the fields is empty")

        # Check if both fields are filled correctly
        elif username == "admin" and password == "password":
            QMessageBox.information(self, "Success", "Login successful")

        # Check if one of the fields is filled correctly
        elif (username == "admin" and password != "password") or (username != "admin" and password == "password"):
            QMessageBox.critical(self, "Error", "One of the fields is filled correctly")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the login window
    window = LoginWindow()
    window.show()

    # Running the application
    sys.exit(app.exec_())
