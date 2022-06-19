import random
from typing import List

from fluxatlas.model import MicroProject, WorkspacePulse

_DOMAINS = ["Web2 tooling", "Web3 finance", "AI research", "bot orchestration", "utility scripting"]
_MOODS = ["curious", "skeptical", "restless", "playful", "focused"]
_PILLARS = ["latency checks", "storyboarding", "small experiments", "pseudo docs", "demo data"]
_STACKS = ["Spring WebFlux", "Rust+WASM", "Python scripts", "GPT helper", "Deno CLI"]


def _pick(items: List[str]) -> str:
    return random.choice(items)


def sketch_microproject() -> MicroProject:
    domain = _pick(_DOMAINS)
    mood = _pick(_MOODS)
    title = f"{mood.title()} {domain.split()[0]} Insight"

    pillars = random.sample(_PILLARS, 3)
    notes = [f"Trial {n+1}: {domain.lower()} + {random.choice(_STACKS)}" for n in range(3)]
    stack = random.sample(_STACKS, 2)

    return MicroProject(title=title, domain=domain, mood=mood, pillars=pillars, notes=notes, stack=stack)


def capture_pulse(epoch: str) -> WorkspacePulse:
    focus = _pick(["researching APIs", "drafting README bits", "debugging mock data", "capturing prompts"])
    energy = _pick(["high", "drifting", "steady", "surprised"])
    tasks = [f"Log idea {i+1}" for i in range(2)]
    return WorkspacePulse(timestamp=epoch, focus=focus, energy_level=energy, tasks=tasks)
