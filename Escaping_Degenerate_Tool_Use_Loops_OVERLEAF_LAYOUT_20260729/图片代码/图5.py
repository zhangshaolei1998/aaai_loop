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
NO_REPEAT_SCORES = [20.2, 60.2, 56.2, 58.5]
SAME_TOOL_REPEAT_SCORES = [25.7, 54.9, 53.9, 58.4]


def main():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "figure.dpi": 160,
            "savefig.dpi": 300,
        }
    )

    figure, axis = plt.subplots(figsize=(10.8, 7.2))
    positions = np.arange(len(MODELS))
    width = 0.34

    no_repeat_bars = axis.bar(
        positions - width / 2,
        NO_REPEAT_SCORES,
        width,
        color="#BDBDBD",
        label="No repeat",
    )
    repeat_bars = axis.bar(
        positions + width / 2,
        SAME_TOOL_REPEAT_SCORES,
        width,
        color="#2C7FB8",
        label="Same-tool repeat",
    )

    for bars, values in (
        (no_repeat_bars, NO_REPEAT_SCORES),
        (repeat_bars, SAME_TOOL_REPEAT_SCORES),
    ):
        for bar, value in zip(bars, values):
            axis.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.8,
                f"{value:.1f}",
                ha="center",
                va="bottom",
                fontsize=15,
                color="#111111",
            )

    axis.set_ylim(0, 75)
    axis.set_ylabel("Scores (%)", fontsize=20, labelpad=12)
    axis.set_xticks(positions)
    axis.set_xticklabels(MODELS, fontsize=14)
    axis.tick_params(axis="y", labelsize=17)
    axis.grid(axis="y", color="#D9D9D9", linewidth=1.0)
    axis.set_axisbelow(True)
    for spine in axis.spines.values():
        spine.set_linewidth(1.7)
        spine.set_color("#111111")

    axis.legend(loc="upper left", frameon=False, fontsize=17)
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "图5.png", bbox_inches="tight", facecolor="white")
    figure.savefig(OUTPUT_DIR / "图5.pdf", bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
