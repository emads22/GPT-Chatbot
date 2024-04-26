from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QLineEdit, QTextEdit, QPushButton


class ChatbotMainWindow(QMainWindow):
    """Main window class for the GPT Chatbot application."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("GPT Chatbot")  # Setting the window title
        # Setting the minimum size for the window
        self.setFixedSize(605, 490)

        # Creating a QTextEdit widget for displaying chat messages
        self.chat_area = QTextEdit(self)
        # Setting the geometry (x, y, width, height) of the QTextEdit widget
        self.chat_area.setGeometry(10, 10, 585, 420)
        # Making the QTextEdit widget read-only
        self.chat_area.setReadOnly(True)

        # Creating a QLineEdit widget for user input
        self.input_text = QLineEdit(self)
        # Setting the geometry of the QLineEdit widget
        self.input_text.setGeometry(10, 440, 485, 40)

        # Creating a QPushButton widget for sending messages
        self.button = QPushButton("Send", self)
        # Setting the geometry of the QPushButton widget
        self.button.setGeometry(505, 440, 90, 40)

        # Call self.show() to display the window when an instance is created
        self.show()
