from enum import Enum
import os
from drawlib.apis import config, save

from src.settings import get_repo_root


class Unit(Enum):
    INCHES = "in"
    CENTIMETERS = "cm"
    MILLIMETERS = "mm"

    def __str__(self):
        return self.value

    @classmethod
    def from_str(cls, s: str) -> "Unit":
        s = s.strip().lower()
        if s in ("in", '"', "inches"):
            return cls.INCHES
        if s in ("cm", "centimeters"):
            return cls.CENTIMETERS
        if s in ("mm", "millimeters"):
            return cls.MILLIMETERS
        raise ValueError(f"Unknown unit: {s}")


class PuzzleDimensions:
    def __init__(self, pieces_width: int, pieces_height: int):
        self.pw = pieces_width
        self.ph = pieces_height


class Canvas:
    def __init__(
        self, width: int, height: int, units: Unit, piece_dimensions: PuzzleDimensions
    ) -> None:
        self.width = width
        self.height = height

        self.units = units
        self.piece_dimensions = piece_dimensions

    def create_canvas(self) -> None:
        config(width=self.width, height=self.height)

    def show_image_preview(self) -> None:
        preview_filepath = os.path.join(get_repo_root(), "canvas_preview.png")
        save(preview_filepath, format="png")