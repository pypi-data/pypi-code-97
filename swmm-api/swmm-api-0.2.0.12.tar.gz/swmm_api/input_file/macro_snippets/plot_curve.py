from swmm_api.input_file.sections import Curve
import matplotlib.pyplot as plt
from numpy import ceil, append, arange, array, concatenate


# def _custom_round(x_, base):
#     return base * ceil(float(x_) / base)


def curve_figure(curve: Curve):
    fig, ax = plt.subplots()

    # -------------------------
    xlim = 1
    ylim = 1
    base = 0.2
    xlim_left = -xlim

    # -------------------------
    y_label, x_label = curve._get_names(curve.Type)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title('{}: {}'.format(curve.Name, curve.Type))

    # -------------------------
    y, x = list(zip(*curve.points))

    y = array(y)
    x = array(x) / 2

    y = concatenate(([0], y, [1]))
    x = concatenate(([0], x, [0]))

    y = append(y, y[::-1])
    x = append(x, x[::-1] * -1)

    # -------------------------
    ax.plot(x, y, marker='.', ls='-', zorder=1000000, clip_on=False)

    # -------------------------
    # ax.legend().remove()
    ax.set_aspect('equal', 'box')
    ax.set_xticks(arange(xlim_left, xlim, base), minor=False)
    if base / 2 != 0:
        ax.set_xticks(arange(xlim_left, xlim, base / 2), minor=True)

    ax.set_yticks(arange(0, ylim, base), minor=False)
    if base / 2 != 0:
        ax.set_yticks(arange(0, ylim, base / 2), minor=True)

    ax.tick_params(which='both', length=0, width=0, labelbottom=False, labeltop=False, labelleft=False,
                   labelright=False, bottom=False, top=False, left=False, right=False)

    ax.set_xlim(xlim_left, xlim)
    ax.set_ylim(0, ylim)
    ax.grid(True)
    # ax.grid(True, which='minor', linestyle=':', linewidth=0.5)
    ax.set_axisbelow(True)

    # ------------------
    fig.tight_layout()
    return fig
