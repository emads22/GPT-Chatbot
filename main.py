from PyQt6.QtWidgets import QApplication
import sys
from ui import IntelliByteMainWindow


def main():
    # Initialize the PyQt application
    app = QApplication(sys.argv)
    # Set the application style to "Fusion" for a consistent look across platforms
    app.setStyle("Fusion")
    # Create an instance of the main window for the chatbot
    main_window = IntelliByteMainWindow()
    # Start the application's event loop and exit cleanly when it's finished
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
