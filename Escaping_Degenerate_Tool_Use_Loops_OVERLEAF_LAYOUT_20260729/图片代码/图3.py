from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent

# Fixed source data from:
# D:\baseline\agent_eval\results\functional_loop_analysis\cross_benchmark\error_trajectory_fl_20260727\anyfl_error_all_by_benchmark_deepseek_flash_state_aligned_invalid_as_failure.csv
# Metric: Functional Loop rate among failed trajectories (%).
BENCHMARKS = ["Shopping", "STATE", "TAU"]
FUNCTIONAL_LOOP_RATE = [75.980392, 5.050505, 52.789700]


def main() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.linewidth": 1.0,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "figure.dpi": 300,
        "savefig.dpi": 300,
    })

    fig, ax = plt.subplots(figsize=(6.8, 3.8), constrained_layout=False)
    x = np.arange(len(BENCHMARKS))
    bars = ax.bar(
        x,
        FUNCTIONAL_LOOP_RATE,
        width=0.50,
        color="#5AB0E6",
        edgecolor="white",
        linewidth=0.7,
        label="Functional Loop",
    )

    for bar, value in zip(bars, FUNCTIONAL_LOOP_RATE):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.8,
            f"{value:.1f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="#333333",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(BENCHMARKS, fontsize=11)
    ax.set_ylabel("Failed trajectories (%)", fontsize=12)
    ax.set_ylim(0, 90)
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    ax.spines["left"].set_linewidth(1.0)
    ax.spines["bottom"].set_linewidth(1.0)
    ax.legend(frameon=False, fontsize=10, loc="upper right")
    fig.subplots_adjust(left=0.13, right=0.98, top=0.95, bottom=0.18)

    fig.savefig(OUT / "图3.png", bbox_inches="tight")
    fig.savefig(OUT / "图3.pdf", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
