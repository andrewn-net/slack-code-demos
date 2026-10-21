"""The block-letter banner across the top of ./demo.

Letters are drawn in the "ANSI Shadow" style: solid blocks with a box-drawn
shadow. Each row takes the next colour of the gradient (purple at the top,
amber at the bottom) and the shadow lines a dimmer shade of it, then a
gradient rule runs underneath. Windows too narrow for those letters get the
same words in a two-row block font (SMALL), coloured left to right; the app
hides the banner when the window is too short for it.
"""
from __future__ import annotations

from rich.text import Text
from textual.events import Resize
from textual.widget import Widget

from demokit.tui.palette import BG, GRADIENT, along, mix

FONT: dict[str, tuple[str, ...]] = {
    "A": (" █████╗ ",
          "██╔══██╗",
          "███████║",
          "██╔══██║",
          "██║  ██║",
          "╚═╝  ╚═╝"),
    "C": (" ██████╗",
          "██╔════╝",
          "██║     ",
          "██║     ",
          "╚██████╗",
          " ╚═════╝"),
    "D": ("██████╗ ",
          "██╔══██╗",
          "██║  ██║",
          "██║  ██║",
          "██████╔╝",
          "╚═════╝ "),
    "E": ("███████╗",
          "██╔════╝",
          "█████╗  ",
          "██╔══╝  ",
          "███████╗",
          "╚══════╝"),
    "K": ("██╗  ██╗",
          "██║ ██╔╝",
          "█████╔╝ ",
          "██╔═██╗ ",
          "██║  ██╗",
          "╚═╝  ╚═╝"),
    "L": ("██╗     ",
          "██║     ",
          "██║     ",
          "██║     ",
          "███████╗",
          "╚══════╝"),
    "M": ("███╗   ███╗",
          "████╗ ████║",
          "██╔████╔██║",
          "██║╚██╔╝██║",
          "██║ ╚═╝ ██║",
          "╚═╝     ╚═╝"),
    "O": (" ██████╗ ",
          "██╔═══██╗",
          "██║   ██║",
          "██║   ██║",
          "╚██████╔╝",
          " ╚═════╝ "),
    "S": ("███████╗",
          "██╔════╝",
          "███████╗",
          "╚════██║",
          "███████║",
          "╚══════╝"),
    " ": ("  ",) * 6,
}
ROWS = 6

# The same letters two rows tall, for windows too narrow for FONT.
SMALL: dict[str, tuple[str, str]] = {
    "A": ("▄▀█", "█▀█"),
    "C": ("█▀▀", "█▄▄"),
    "D": ("█▀▄", "█▄▀"),
    "E": ("█▀▀", "██▄"),
    "K": ("█▄▀", "█ █"),
    "L": ("█  ", "█▄▄"),
    "M": ("█▀▄▀█", "█ ▀ █"),
    "O": ("█▀█", "█▄█"),
    "S": ("█▀▀", "▄▄█"),
    " ": ("  ", "  "),
}

WORD = "SLACK CODE DEMOS"
PAD = 2  # columns left of the letters


def art(word: str = WORD) -> list[str]:
    """``word`` in block letters, one string per row."""
    return ["".join(FONT[ch][row] for ch in word) for row in range(ROWS)]


def small_art(word: str = WORD) -> list[str]:
    """``word`` in the two-row font, a column between letters."""
    return [" ".join(SMALL[ch][row] for ch in word) for row in range(2)]


def width(word: str = WORD) -> int:
    return len(art(word)[0])


def fits_big(columns: int) -> bool:
    return width() + PAD <= columns


class Banner(Widget):
    DEFAULT_CSS = "Banner { height: 7; width: 1fr; }"

    def on_resize(self, event: Resize) -> None:
        self.styles.height = 7 if fits_big(event.size.width) else 3

    def render(self) -> Text:
        room = self.size.width
        out = Text(no_wrap=True, overflow="crop")
        if fits_big(room):
            for row, line in enumerate(art()):
                solid = GRADIENT[row]
                shadow = mix(solid, BG, 0.45)
                out.append(" " * PAD)
                for ch in line:
                    out.append(ch, style=solid if ch == "█" else shadow)
                out.append("\n")
        else:
            for line in small_art():
                out.append(" " * PAD)
                for i, ch in enumerate(line):
                    out.append(ch, style=along(i / max(len(line) - 1, 1)))
                out.append("\n")
        rule = max(room - PAD, 1)
        out.append(" " * PAD)
        for i in range(rule):
            out.append("━", style=along(i / max(rule - 1, 1)))
        return out
