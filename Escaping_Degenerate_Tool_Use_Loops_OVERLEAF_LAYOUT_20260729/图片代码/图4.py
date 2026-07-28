from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent

MODELS = [
    "Qwen3-\n14B",
    "DeepSeek-v4-\nFlash",
    "MiMo-v2.5-\nPro",
    "DeepSeek-v4-\nPro",
]
SCORES_NO_FUNCTIONAL_LOOP = [25.5, 56.6, 54.8, 58.6]
SCORES_FUNCTIONAL_LOOP = [17.9, 41.2, 50.0, 50.0]
CALLS_NO_FUNCTIONAL_LOOP = [4.4, 7.8, 6.1, 7.0]
CALLS_FUNCTIONAL_LOOP = [11.4, 16.5, 13.0, 12.4]


def add_value_labels(axis, bars, values):
    for bar, value in zip(bars, values):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.8,
            f"{value:.1f}",
            ha="center",
            va="bottom",
            fontsize=13,
            color="#222222",
        )


def style_axis(axis, ylabel):
    axis.set_ylabel(ylabel, fontsize=16, labelpad=10)
    axis.set_xticks(np.arange(len(MODELS)))
    axis.set_xticklabels(MODELS, fontsize=12.5)
    axis.tick_params(axis="y", labelsize=13)
    axis.grid(axis="y", color="#D9D9D9", linewidth=1.0)
    axis.set_axisbelow(True)
    for spine in axis.spines.values():
        spine.set_linewidth(1.6)
        spine.set_color("#111111")


def main():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "figure.dpi": 160,
            "savefig.dpi": 300,
        }
    )

    figure, axes = plt.subplots(1, 2, figsize=(13.0, 5.6))
    positions = np.arange(len(MODELS))
    width = 0.34

    score_no_loop = axes[0].bar(
        positions - width / 2,
        SCORES_NO_FUNCTIONAL_LOOP,
        width,
        color="#BDBDBD",
        label="No Functional Loop",
    )
    score_loop = axes[0].bar(
        positions + width / 2,
        SCORES_FUNCTIONAL_LOOP,
        width,
        color="#2C7FB8",
        label="Functional Loop",
    )
    style_axis(axes[0], "Score (%)")
    axes[0].set_ylim(0, 70)
    add_value_labels(axes[0], score_no_loop, SCORES_NO_FUNCTIONAL_LOOP)
    add_value_labels(axes[0], score_loop, SCORES_FUNCTIONAL_LOOP)
    axes[0].legend(loc="upper left", frameon=False, fontsize=14)

    calls_no_loop = axes[1].bar(
        positions - width / 2,
        CALLS_NO_FUNCTIONAL_LOOP,
        width,
        color="#BDBDBD",
        label="No Functional Loop",
    )
    calls_loop = axes[1].bar(
        positions + width / 2,
        CALLS_FUNCTIONAL_LOOP,
        width,
        color="#F2A900",
        label="Functional Loop",
    )
    style_axis(axes[1], "Calls / trajectory")
    axes[1].set_ylim(0, 18.5)
    add_value_labels(axes[1], calls_no_loop, CALLS_NO_FUNCTIONAL_LOOP)
    add_value_labels(axes[1], calls_loop, CALLS_FUNCTIONAL_LOOP)
    axes[1].legend(loc="upper right", frameon=False, fontsize=14)

    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "图4.png", bbox_inches="tight", facecolor="white")
    figure.savefig(OUTPUT_DIR / "图4.pdf", bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
