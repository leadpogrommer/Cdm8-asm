from dataclasses import dataclass


@dataclass
class CodeLocation:
    file: str
    line: int
    column: int
