from enum import Enum

class Orientation(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def from_str(cls, s: str) -> "Orientation":
        s = s.strip().lower()
        if s in ("h", "horizontal"):
            return cls.HORIZONTAL
        if s in ("v", "vertical"):
            return cls.VERTICAL
        raise ValueError(f"Unknown orientation: {s}")