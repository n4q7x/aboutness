"""App entrypoint."""

import sys

from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QMainWindow

from aboutness.ui.layout import build_central_widget


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Aboutness Canvas")

    # Central content: canvas on the left, right panel, bottom panel.
    window.setCentralWidget(build_central_widget())

    # macOS-friendly close shortcut (Cmd+W).
    QShortcut(QKeySequence.StandardKey.Close, window, activated=window.close)

    window.resize(1000, 700)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
