from views import pageController
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    window = QApplication(sys.argv)
    view = pageController.PageController()
    sys.exit(window.exec())