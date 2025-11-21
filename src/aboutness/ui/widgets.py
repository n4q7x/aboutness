"""UI widgets for Aboutness."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout, QWidget


class Canvas(QWidget):
    """Empty canvas widget."""

    def __init__(self):
        super().__init__()
        # Leave unstyled; it just fills the available space.


class Panel(QFrame):
    """Simple framed panel with an optional label."""

    def __init__(self, title: str = ""):
        super().__init__()
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(1)

        layout = QVBoxLayout()
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setAlignment(Qt.AlignCenter)

        if title:
            label = QLabel(title)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        self.setLayout(layout)
