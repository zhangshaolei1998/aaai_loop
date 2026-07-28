"""Figure 9: STATE-Bench interaction cost on the Raw Any-FL subset."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent

MODELS = [
    "Ministral-3-14B\nInstruct-2512",
    "Qwen3-14B",
    "DeepSeek-v4-Flash",
    "MiMo-v2.5-pro",
    "DeepSeek-v4-Pro",
]
RAW_CALLS = [12.859375, 10.4733727811, 16.4705882353, 13.0, 12.4]
PERSIST_ACE_CALLS = [10.34375, 9.8224852071, 15.0588235294, 9.875, 10.4]

RAW_COLOR = "#BDBDBD"
PERSIST_ACE_COLOR = "#2C7FB8"


def add_labels(axis, bars, values):
    for bar, value in zip(bars, values):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.35,
            f"{value:.1f}",
            ha="center",
            va="bottom",
            fontsize=13,
            color="#222222",
        )


def main():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "figure.dpi": 160,
            "savefig.dpi": 300,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    x_positions = np.arange(len(MODELS))
    width = 0.34
    figure, axis = plt.subplots(figsize=(11.8, 5.2))

    raw_bars = axis.bar(
        x_positions - width / 2,
        RAW_CALLS,
        width,
        color=RAW_COLOR,
        edgecolor="white",
        linewidth=0.8,
        label="Raw",
    )
    persist_bars = axis.bar(
        x_positions + width / 2,
        PERSIST_ACE_CALLS,
        width,
        color=PERSIST_ACE_COLOR,
        edgecolor="white",
        linewidth=0.8,
        label="PERSIST-ACE",
    )

    axis.set_ylim(0, 21)
    axis.set_ylabel("Calls / trajectory", fontsize=16, labelpad=10)
    axis.set_xticks(x_positions)
    axis.set_xticklabels(MODELS, fontsize=15)
    axis.tick_params(axis="y", labelsize=13)
    axis.grid(axis="y", color="#D9D9D9", linewidth=1.0)
    axis.set_axisbelow(True)
    for spine in axis.spines.values():
        spine.set_linewidth(1.6)
        spine.set_color("#111111")

    add_labels(axis, raw_bars, RAW_CALLS)
    add_labels(axis, persist_bars, PERSIST_ACE_CALLS)
    axis.legend(
        loc="upper right",
        bbox_to_anchor=(0.985, 0.985),
        frameon=False,
        fontsize=14,
        ncol=2,
    )

    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "图9.png", bbox_inches="tight", facecolor="white")
    figure.savefig(OUTPUT_DIR / "图9.pdf", bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
