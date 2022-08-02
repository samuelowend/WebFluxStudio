from typing import Iterable

from fluxatlas.model import MicroProject, WorkspacePulse


def render_project(project: MicroProject) -> str:
    lines = ["Project Sketch", "-----------", f"Title: {project.title}", f"Domain: {project.domain}", f"Mood: {project.mood}"]
    lines.append("Pillars:")
    lines.extend([f"  - {p}" for p in project.pillars])
    lines.append("Stack:")
    lines.extend([f"  - {s}" for s in project.stack])
    lines.append("Notes:")
    lines.extend([f"  * {n}" for n in project.notes])
    return "\n".join(lines)


def render_pulse(pulse: WorkspacePulse) -> str:
    tasks = "\n".join([f"    • {task}" for task in pulse.tasks])
    return (
        f"Workspace Pulse @ {pulse.timestamp}\n"
        f"Focus: {pulse.focus}\n"
        f"Energy: {pulse.energy_level}\n"
        f"Tasks:\n{tasks}"
    )


def render_pulse_series(series: Iterable[WorkspacePulse]) -> str:
    return "\n\n".join(render_pulse(p) for p in series)
