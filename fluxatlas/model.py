from dataclasses import dataclass
from typing import List

@dataclass
class MicroProject:
    title: str
    domain: str
    mood: str
    pillars: List[str]
    notes: List[str]
    stack: List[str]

@dataclass
class WorkspacePulse:
    timestamp: str
    focus: str
    energy_level: str
    tasks: List[str]
