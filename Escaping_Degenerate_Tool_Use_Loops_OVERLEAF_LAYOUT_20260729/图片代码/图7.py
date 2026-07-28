"""Figure 7: Net positive gain among triggered STATE-Bench trajectories."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent

# Frozen observed W/T/L counts.
MODELS = [
    "Ministral-3-14B\nInstruct-2512",
    "Qwen3-14B",
    "DeepSeek-v4-Flash",
    "DeepSeek-v4-Pro",
    "MiMo-v2.5-pro",
]
WINS = np.array([8, 2, 13, 6, 10], dtype=float)
TIES = np.array([18, 3, 31, 22, 18], dtype=float)
LOSSES = np.array([2, 1, 1, 3, 2], dtype=float)

TRIGGERED = WINS + TIES + LOSSES
NET_POSITIVE_GAIN = 100.0 * (WINS - LOSSES) / TRIGGERED
OVERALL_GAIN = 100.0 * (WINS.sum() - LOSSES.sum()) / TRIGGERED.sum()

BAR_COLOR = "#0072B2"


def main():
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "figure.dpi": 160,
            "savefig.dpi": 320,
            "axes.labelsize": 14,
            "xtick.labelsize": 13,
            "ytick.labelsize": 11,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    x_positions = np.arange(len(MODELS))
    figure, axis = plt.subplots(figsize=(10.2, 4.35), constrained_layout=True)

    bars = axis.bar(
        x_positions,
        NET_POSITIVE_GAIN,
        width=0.62,
        color=BAR_COLOR,
        edgecolor="white",
        linewidth=0.9,
        zorder=3,
    )

    for bar, value in zip(bars, NET_POSITIVE_GAIN):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.75,
            f"{value:.1f}%",
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
        )

    axis.text(
        0.50,
        0.98,
        f"Overall: ({int(WINS.sum())}-{int(LOSSES.sum())})/"
        f"{int(TRIGGERED.sum())} = {OVERALL_GAIN:.1f}%",
        ha="center",
        va="top",
        fontsize=10,
        color="#555555",
        transform=axis.transAxes,
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85, "pad": 2.5},
    )

    axis.set_ylabel("Net positive gain among triggered trajectories (%)")
    axis.set_xticks(x_positions, MODELS)
    axis.set_ylim(0, 32)
    axis.set_yticks(np.arange(0, 31, 5))
    axis.grid(axis="y", color="#D9DDE2", linewidth=0.9, alpha=0.8, zorder=0)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)

    figure.savefig(OUTPUT_DIR / "图7.png", bbox_inches="tight", facecolor="white")
    figure.savefig(OUTPUT_DIR / "图7.pdf", bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
