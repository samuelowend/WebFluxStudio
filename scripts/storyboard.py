from datetime import datetime, timedelta

from fluxatlas.core import capture_pulse, sketch_microproject
from fluxatlas.insights import render_insight_summary, summarize_workspace
from fluxatlas.renderer import render_project, render_pulse


def assemble_story() -> str:
    now = datetime.utcnow()
    pulses = []
    captures = []

    for offset in range(3):
        stamp = (now - timedelta(days=offset)).isoformat(timespec="seconds")
        pulses.append(capture_pulse(stamp))
        captures.append(sketch_microproject())

    fragments = [
        render_project(captures[idx]) + "\n\n" + render_pulse(pulses[idx])
        for idx in range(len(captures))
    ]
    insight_header = render_insight_summary(summarize_workspace(captures, pulses))
    fragments.append(insight_header)

    return "\n\n".join(fragments)


if __name__ == "__main__":
    print(assemble_story())
