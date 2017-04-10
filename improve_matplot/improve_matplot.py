import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# get scaled font sizes relative to figure size
def getFontSizes(fig):
    fpix = fig.get_size_inches()*fig.dpi
    txfontsize = fpix[1]/105.56
    lbfontsize = fpix[1]/135.71
    return txfontsize, lbfontsize

# make axis look tolerable
def beautifyAx(fig, ax, xmin, xmax, ymin, ymax,
               plt_title, xlabel, ylabel, **kwargs):
    txfontsize, lbfontsize = getFontSizes(fig)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    ax.set_title(plt_title, x=0.0, y=1.02, horizontalalignment='left', fontsize=txfontsize)

    panind = 3

    # for 4 panel plot: use panind kwarg to plot xlabel, ylabel or not
    if 'panind' in kwargs:
        panind = kwargs['panind']
    if panind==3 or panind==4:
        ax.set_xlabel(xlabel, fontsize=txfontsize)
    if panind==3 or panind==1:
        ax.set_ylabel(ylabel, fontsize=txfontsize, labelpad=20)

    # change tick mark sizes and fonts
    ax.tick_params(axis='both', which='major', labelsize=lbfontsize, pad=20)
    ax.set_xticklabels(ax.get_xticks())
    ax.set_yticklabels(ax.get_yticks())
    ax.grid(color='k', linestyle=(0.5, [2,6]), linewidth=1.)
    return

# make colorbar look tolerable
def beautifyCbar(fig, cb, cb_label):
    txfontsize, lbfontsize = getFontSizes(fig)
    cb.set_label(cb_label, fontsize=txfontsize)
    cb_la = [ti.get_text().replace('$', '') for ti in cb.ax.get_yticklabels()]
    cb.ax.set_yticklabels(cb_la, fontsize=lbfontsize)

# make custom tickmarks
def makeTicks(plt, xmin, xmax, ymin, ymax):
    # create tickmark arrays
    numxtick = 4
    numytick = 4
    xtickstep = int((xmax-xmin)/numxtick)
    ytickstep = int((ymax-ymin)/numytick)
    xticks = np.arange(xmin, xmax, xtickstep)
    yticks = np.arange(ymin, ymax, ytickstep)

    # draw tickmarks
    plt.xticks(xticks)
    plt.yticks(yticks)
    return

# use helvetica instead of default font
def adjustFonts(mpl):
    mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    mpl.rc('text', usetex=True)
    return

