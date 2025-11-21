"""Minimal PySide6 desktop canvas app."""

from __future__ import annotations

import sys

from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


class Canvas(QWidget):
    """Simple canvas that lets you place dots with left clicks."""

    def __init__(self) -> None:
        super().__init__()
        self._points: list[QPointF] = []
        self.setMinimumSize(640, 480)
        self.setAutoFillBackground(True)

    def mousePressEvent(self, event) -> None:  # type: ignore[override]
        if event.button() == Qt.LeftButton:
            # event.position() returns QPointF in Qt6.
            self._points.append(event.position())
            self.update()
        super().mousePressEvent(event)

    def paintEvent(self, event) -> None:  # type: ignore[override]
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        pen = QPen(Qt.black, 4)
        painter.setPen(pen)
        for point in self._points:
            painter.drawPoint(point.toPoint())
        super().paintEvent(event)


def main() -> None:
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Aboutness Canvas")
    window.resize(800, 600)
    canvas = Canvas()
    window.setCentralWidget(canvas)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
