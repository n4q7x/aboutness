"""Layout composition for the Aboutness UI."""

from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from .widgets import Canvas, Panel


def build_central_widget() -> QWidget:
    """Assemble main canvas with right and bottom panels."""
    central = QWidget()

    # Outer column: top row + bottom panel.
    outer_v = QVBoxLayout()
    outer_v.setContentsMargins(0, 0, 0, 0)
    outer_v.setSpacing(0)
    central.setLayout(outer_v)

    # Top row: canvas + right panel.
    top_row = QHBoxLayout()
    top_row.setContentsMargins(0, 0, 0, 0)
    top_row.setSpacing(0)

    canvas = Canvas()
    right_panel = Panel(title="Right panel")
    right_panel.setMinimumWidth(180)

    top_row.addWidget(canvas, stretch=3)
    top_row.addWidget(right_panel, stretch=1)

    # Bottom panel.
    bottom_panel = Panel(title="Bottom panel")
    bottom_panel.setMinimumHeight(140)

    outer_v.addLayout(top_row, stretch=3)
    outer_v.addWidget(bottom_panel, stretch=1)

    return central
