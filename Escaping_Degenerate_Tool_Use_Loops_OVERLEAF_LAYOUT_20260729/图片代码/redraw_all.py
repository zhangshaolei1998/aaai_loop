"""Redraw all bar-chart figures for main2.tex in a unified academic style.

Outputs are written directly to ../figures/ (both .png and .pdf).
No titles, thin spines, y-grid only, serif font, consistent palette.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
FIG_DIR = HERE.parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

COLOR_BASELINE = "#B8B8B8"
COLOR_MAIN = "#2A5EA8"
COLOR_ACCENT = "#D9740B"
COLOR_SINGLE = "#3A6EA5"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.linewidth": 0.9,
    "xtick.labelsize": 10.5,
    "ytick.labelsize": 10.5,
    "legend.fontsize": 11,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "figure.dpi": 150,
    "savefig.dpi": 300,
})


def clean_axes(ax):
    ax.grid(axis="y", color="#DBDBDB", linewidth=0.7, linestyle="-", alpha=0.95)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.9)
    ax.spines["bottom"].set_linewidth(0.9)
    ax.tick_params(direction="out", length=3.5, width=0.9)


def add_bar_labels(ax, bars, values, fmt="{:.1f}", pad=0.6, fontsize=9.5):
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + pad,
                fmt.format(v),
                ha="center", va="bottom",
                fontsize=fontsize, color="#222222")


def save(fig, name):
    fig.savefig(FIG_DIR / f"{name}.png", bbox_inches="tight", facecolor="white")
    fig.savefig(FIG_DIR / f"{name}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def fig_prev_by_model():
    MODELS = ["Qwen3-14B", "DeepSeek-v4-\nFlash", "MiMo-v2.5-\nPro", "DeepSeek-v4-\nPro"]
    RATE = [35.17, 5.05, 3.92, 2.67]
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    x = np.arange(len(MODELS))
    bars = ax.bar(x, RATE, width=0.55, color=COLOR_SINGLE,
                  edgecolor="white", linewidth=0.6)
    add_bar_labels(ax, bars, RATE, fmt="{:.1f}%", pad=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(MODELS)
    ax.set_ylabel("Functional Loop rate (%)")
    ax.set_ylim(0, 42)
    clean_axes(ax)
    fig.tight_layout()
    save(fig, "fig_prevalence_by_model")


def fig_prev_by_benchmark():
    BENCHMARKS = ["STATE-Bench", "$\\tau$-Knowledge", "DeepPlanning\nShopping"]
    RATE = [5.05, 52.79, 75.98]
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    x = np.arange(len(BENCHMARKS))
    bars = ax.bar(x, RATE, width=0.5, color=COLOR_ACCENT,
                  edgecolor="white", linewidth=0.6)
    add_bar_labels(ax, bars, RATE, fmt="{:.1f}%", pad=1.2)
    ax.set_xticks(x)
    ax.set_xticklabels(BENCHMARKS)
    ax.set_ylabel("Functional Loop rate (%)")
    ax.set_ylim(0, 90)
    clean_axes(ax)
    fig.tight_layout()
    save(fig, "fig_prevalence_by_benchmark")


def fig4():
    MODELS = ["Qwen3-14B", "DeepSeek-v4-\nFlash", "MiMo-v2.5-\nPro", "DeepSeek-v4-\nPro"]
    SCORES_NO = [25.5, 56.6, 54.8, 58.6]
    SCORES_FL = [17.9, 41.2, 50.0, 50.0]
    CALLS_NO = [4.4, 7.8, 6.1, 7.0]
    CALLS_FL = [11.4, 16.5, 13.0, 12.4]
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.7))
    x = np.arange(len(MODELS))
    w = 0.36

    ax = axes[0]
    b1 = ax.bar(x - w / 2, SCORES_NO, w, color=COLOR_BASELINE,
                edgecolor="white", linewidth=0.6, label="No Functional Loop")
    b2 = ax.bar(x + w / 2, SCORES_FL, w, color=COLOR_MAIN,
                edgecolor="white", linewidth=0.6, label="Functional Loop")
    add_bar_labels(ax, b1, SCORES_NO)
    add_bar_labels(ax, b2, SCORES_FL)
    ax.set_xticks(x)
    ax.set_xticklabels(MODELS)
    ax.set_ylabel("STATE-Bench score (%)")
    ax.set_ylim(0, 72)
    ax.legend(frameon=False, loc="upper left")
    clean_axes(ax)

    ax = axes[1]
    b1 = ax.bar(x - w / 2, CALLS_NO, w, color=COLOR_BASELINE,
                edgecolor="white", linewidth=0.6, label="No Functional Loop")
    b2 = ax.bar(x + w / 2, CALLS_FL, w, color=COLOR_ACCENT,
                edgecolor="white", linewidth=0.6, label="Functional Loop")
    add_bar_labels(ax, b1, CALLS_NO, pad=0.25)
    add_bar_labels(ax, b2, CALLS_FL, pad=0.25)
    ax.set_xticks(x)
    ax.set_xticklabels(MODELS)
    ax.set_ylabel("Tool calls per trajectory")
    ax.set_ylim(0, 20)
    ax.legend(frameon=False, loc="upper right")
    clean_axes(ax)

    fig.tight_layout()
    save(fig, "fig_fl_statebench_consequences")


def fig5():
    MODELS = ["Qwen3-14B", "DeepSeek-v4-\nFlash", "MiMo-v2.5-\nPro", "DeepSeek-v4-\nPro"]
    NO_REP = [20.2, 60.2, 56.2, 58.5]
    REP = [25.7, 54.9, 53.9, 58.4]
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    x = np.arange(len(MODELS))
    w = 0.36
    b1 = ax.bar(x - w / 2, NO_REP, w, color=COLOR_BASELINE,
                edgecolor="white", linewidth=0.6, label="No repeat")
    b2 = ax.bar(x + w / 2, REP, w, color=COLOR_MAIN,
                edgecolor="white", linewidth=0.6, label="Same-tool repeat")
    add_bar_labels(ax, b1, NO_REP)
    add_bar_labels(ax, b2, REP)
    ax.set_xticks(x)
    ax.set_xticklabels(MODELS)
    ax.set_ylabel("STATE-Bench score (%)")
    ax.set_ylim(0, 75)
    ax.legend(frameon=False, loc="upper left")
    clean_axes(ax)
    fig.tight_layout()
    save(fig, "fig_statebench_same_tool_repeat")


def fig7():
    MODELS = ["Ministral-3-\n14B", "Qwen3-14B", "DeepSeek-v4-\nFlash",
              "DeepSeek-v4-\nPro", "MiMo-v2.5-\nPro"]
    W = np.array([8, 2, 13, 6, 10], dtype=float)
    T = np.array([18, 3, 31, 22, 18], dtype=float)
    L = np.array([2, 1, 1, 3, 2], dtype=float)
    N = W + T + L
    GAIN = 100.0 * (W - L) / N
    OVERALL = 100.0 * (W.sum() - L.sum()) / N.sum()

    fig, ax = plt.subplots(figsize=(8.0, 3.5))
    x = np.arange(len(MODELS))
    bars = ax.bar(x, GAIN, width=0.55, color=COLOR_MAIN,
                  edgecolor="white", linewidth=0.6)
    for bar, v in zip(bars, GAIN):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.55,
                f"{v:.1f}%", ha="center", va="bottom",
                fontsize=10.5, color="#111111")
    ax.axhline(OVERALL, color=COLOR_ACCENT, linewidth=1.2, linestyle="--",
               alpha=0.9, label=f"Overall = {OVERALL:.1f}%")
    ax.set_xticks(x)
    ax.set_xticklabels(MODELS)
    ax.set_ylabel("Net outcome margin\n$(W-L)/N_{\\mathrm{triggered}}$ (%)")
    ax.set_ylim(0, 32)
    ax.legend(frameon=False, loc="upper right")
    clean_axes(ax)
    fig.tight_layout()
    save(fig, "fig_statebench_triggered_failure_recovery")


def fig8():
    MODELS = ["Ministral-3-\n14B", "Qwen3-14B", "DeepSeek-v4-\nFlash",
              "MiMo-v2.5-\nPro", "DeepSeek-v4-\nPro"]
    RAW = [17.19, 19.53, 41.18, 50.00, 50.00]
    LB = [26.56, 23.08, 47.06, 68.75, 60.00]
    fig, ax = plt.subplots(figsize=(8.6, 3.7))
    x = np.arange(len(MODELS))
    w = 0.36
    b1 = ax.bar(x - w / 2, RAW, w, color=COLOR_BASELINE,
                edgecolor="white", linewidth=0.6, label="Baseline")
    b2 = ax.bar(x + w / 2, LB, w, color=COLOR_MAIN,
                edgecolor="white", linewidth=0.6, label="LoopBreaker")
    add_bar_labels(ax, b1, RAW)
    add_bar_labels(ax, b2, LB)
    ax.set_xticks(x)
    ax.set_xticklabels(MODELS)
    ax.set_ylabel("STATE-Bench score (%)")
    ax.set_ylim(0, 85)
    ax.legend(frameon=False, loc="upper left", ncol=2)
    clean_axes(ax)
    fig.tight_layout()
    save(fig, "fig_statebench_fl_subset_scores")


def fig9():
    MODELS = ["Ministral-3-\n14B", "Qwen3-14B", "DeepSeek-v4-\nFlash",
              "MiMo-v2.5-\nPro", "DeepSeek-v4-\nPro"]
    RAW = [12.86, 10.47, 16.47, 13.00, 12.40]
    LB = [10.34, 9.82, 15.06, 9.88, 10.40]
    fig, ax = plt.subplots(figsize=(8.6, 3.7))
    x = np.arange(len(MODELS))
    w = 0.36
    b1 = ax.bar(x - w / 2, RAW, w, color=COLOR_BASELINE,
                edgecolor="white", linewidth=0.6, label="Baseline")
    b2 = ax.bar(x + w / 2, LB, w, color=COLOR_MAIN,
                edgecolor="white", linewidth=0.6, label="LoopBreaker")
    add_bar_labels(ax, b1, RAW, pad=0.2)
    add_bar_labels(ax, b2, LB, pad=0.2)
    ax.set_xticks(x)
    ax.set_xticklabels(MODELS)
    ax.set_ylabel("Tool calls per trajectory")
    ax.set_ylim(0, 20)
    ax.legend(frameon=False, loc="upper left", ncol=2)
    clean_axes(ax)
    fig.tight_layout()
    save(fig, "fig_statebench_fl_subset_calls")


if __name__ == "__main__":
    for f in (fig_prev_by_model, fig_prev_by_benchmark, fig4, fig5, fig7, fig8, fig9):
        f()
    print(f"[done] figures written to {FIG_DIR}")
