from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Mapping

from fluxatlas.model import MicroProject, WorkspacePulse


@dataclass(frozen=True)
class InsightSummary:
    project_count: int
    domain_counts: Mapping[str, int]
    stack_counts: Mapping[str, int]
    energy_counts: Mapping[str, int]
    focus_counts: Mapping[str, int]


def _group_counter(items: Iterable[str]) -> Mapping[str, int]:
    counter = Counter(items)
    return dict(sorted(counter.items()))


def summarize_workspace(projects: Iterable[MicroProject], pulses: Iterable[WorkspacePulse]) -> InsightSummary:
    project_list = list(projects)
    domain_counts = _group_counter(project.domain for project in project_list)
    stack_counts = _group_counter(stack for project in project_list for stack in project.stack)

    energy_counts = _group_counter(pulse.energy_level for pulse in pulses)
    focus_counts = _group_counter(pulse.focus for pulse in pulses)

    summary = InsightSummary(
        project_count=len(project_list),
        domain_counts=dict(sorted(domain_counts.items())),
        stack_counts=dict(sorted(stack_counts.items())),
        energy_counts=dict(sorted(energy_counts.items())),
        focus_counts=dict(sorted(focus_counts.items())),
    )

    return summary


def render_insight_summary(summary: InsightSummary) -> str:
    def _render(counter: Mapping[str, int]) -> str:
        if not counter:
            return "    (none)"
        return "\n".join(f"    {key}: {value}" for key, value in counter.items())

    return (
        f"Insight Summary ({summary.project_count} sketches)\n"
        f"  Domains:\n{_render(summary.domain_counts)}\n"
        f"  Stacks:\n{_render(summary.stack_counts)}\n"
        f"  Energy:\n{_render(summary.energy_counts)}\n"
        f"  Focus:\n{_render(summary.focus_counts)}"
    )
