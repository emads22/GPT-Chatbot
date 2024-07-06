from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtGui import QFont, QIcon
from backend import Chatbot
from threading import Thread
from constants import LOGO_FILE


class IntelliByteMainWindow(QMainWindow):
    """Main window class for the IntelliByte application."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()

        self.chatbot = Chatbot()

        self.setWindowTitle("IntelliByte")  # Setting the window title
        # Set the window icon
        self.setWindowIcon(QIcon(str(LOGO_FILE)))
        # Setting the fixed size for the window
        self.setFixedSize(605, 490)
        # Create a Qfont object to be used in the window
        font = QFont('Helvetica', 12)

        # Creating a QTextEdit widget for displaying chat messages
        self.chat_area = QTextEdit(self)
        # Setting the geometry (x, y, width, height) of the QTextEdit widget
        self.chat_area.setGeometry(10, 10, 585, 420)
        # Making the QTextEdit widget read-only
        self.chat_area.setReadOnly(True)
        self.chat_area.setFont(font)

        # Creating a QLineEdit widget for user input
        self.input_text = QLineEdit(self)
        # Setting the geometry of the QLineEdit widget
        self.input_text.setGeometry(10, 440, 485, 40)
        self.input_text.setFont(font)
        self.input_text.setText(" ")
        # Connect the returnPressed signal of the input_text QLineEdit widget to the send_message method
        self.input_text.returnPressed.connect(self.send_message)

        # Creating a QPushButton widget for sending messages
        self.button = QPushButton("Send", self)
        # Setting the geometry of the QPushButton widget
        self.button.setGeometry(505, 440, 90, 40)
        self.button.setFont(font)
        self.button.clicked.connect(self.send_message)

        # Call self.show() to display the window when an instance is created
        self.show()

    def send_message(self):
        """
        Sends a message from the user to the chat area and initiates a thread to get the bot's response.
        """
        # Get user input from the input_text QLineEdit widget
        user_input = self.input_text.text().strip()

        # Append the user's message to the chat area with the "Me" label
        # style='color: #333333'
        self.chat_area.append(f"<p><strong>. Me</strong>: {user_input}</p>")

        # Clear the input_text QLineEdit widget
        self.input_text.clear()

        # Create and start a new thread to get the bot's response
        thread = Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        """
        Gets the bot's response to the user's message and appends it to the chat area.

        Args:
            user_input (str): The input text provided by the user.
        """
        # Get the bot's response using the chatbot object
        response = self.chatbot.get_response(user_input)

        # Append the bot's response to the chat area with the "Byte" label
        # style='color: #333333; background-color:E9E9E9'
        self.chat_area.append(f"<p><strong>. Byte</strong>: {response}</p>")
