from fluxatlas.insights import render_insight_summary, summarize_workspace
from fluxatlas.model import MicroProject, WorkspacePulse


def _sample_projects():
    return [
        MicroProject(
            title="Restless AI idea",
            domain="AI research",
            mood="restless",
            pillars=["storyboarding", "demo data", "pseudo docs"],
            notes=["Trial 1", "Trial 2", "Trial 3"],
            stack=["Python scripts", "Rust+WASM"],
        ),
        MicroProject(
            title="Bot orchestration draft",
            domain="bot orchestration",
            mood="curious",
            pillars=["small experiments", "latency checks", "storyboarding"],
            notes=["Trial A", "Trial B", "Trial C"],
            stack=["Deno CLI", "Python scripts"],
        ),
    ]


def _sample_pulses():
    return [
        WorkspacePulse(
            timestamp="2022-03-31T12:02:10",
            focus="researching APIs",
            energy_level="high",
            tasks=["Log idea 1", "Log idea 2"],
        ),
        WorkspacePulse(
            timestamp="2022-03-30T18:15:27",
            focus="debugging mock data",
            energy_level="drifting",
            tasks=["Log idea 3", "Log idea 4"],
        ),
    ]


def test_summarize_workspace_tracks_counts():
    projects = _sample_projects()
    pulses = _sample_pulses()
    summary = summarize_workspace(projects, pulses)

    assert summary.project_count == 2
    assert summary.domain_counts["AI research"] == 1
    assert summary.domain_counts["bot orchestration"] == 1
    assert summary.stack_counts["Python scripts"] == 2
    assert summary.energy_counts["high"] == 1
    assert summary.energy_counts["drifting"] == 1
    assert summary.focus_counts["researching APIs"] == 1
    assert summary.focus_counts["debugging mock data"] == 1


def test_render_insight_summary_mentions_domains():
    projects = _sample_projects()
    pulses = _sample_pulses()
    summary = summarize_workspace(projects, pulses)
    output = render_insight_summary(summary)

    assert "Domains:" in output
    assert "AI research: 1" in output
    assert "Energy:" in output
    assert "drifting: 1" in output
