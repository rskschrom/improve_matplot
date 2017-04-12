import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# class for defining nice looking panel
class Panel:
    def __init__(self, fig, ax, plt, cb):
        self.figure = fig
        self.axis = ax
        self.plot = plt
        self.colorbar = cb
        self.xbounds = []
        self.ybounds = []
        self.txscale = 105.56
        self.lbscale = 135.71
        self.panel_ind = 3

    # set methods
    def set_xbounds(self, xbounds):
        self.xbounds = xbounds

    def set_ybounds(self, ybounds):
        self.ybounds = ybounds

    def set_txscale(self, txscale):
        self.txscale = txscale

    def set_lbscale(self, lbscale):
        self.lbscale = lbscale

    # set panel index (corresponds to position of subplot)
    def set_panel_ind(self, panel_ind):
        self.panel_ind = panel_ind
    
    # get scaled font sizes relative to figure size
    def get_font_sizes(self):
        fpix = self.figure.get_size_inches()*self.figure.dpi

        txfontsize = fpix[1]/self.txscale
        lbfontsize = fpix[1]/self.lbscale
        return txfontsize, lbfontsize

    # make axis look tolerable
    def beautify_axis(self, plt_title, xlabel, ylabel):
        txfontsize, lbfontsize = self.get_font_sizes()
        self.axis.set_xlim(self.xbounds)
        self.axis.set_ylim(self.ybounds)
        self.axis.set_title(plt_title, x=0.0, y=1.02,
                            horizontalalignment='left',
                            fontsize=txfontsize)

        # determine which labels to plot for the panel position
        if self.panel_ind==3 or self.panel_ind==4:
            self.axis.set_xlabel(xlabel, fontsize=txfontsize)
        if self.panel_ind==3 or self.panel_ind==1:
            self.axis.set_ylabel(ylabel, fontsize=txfontsize, labelpad=20)

        # change tick mark sizes and fonts
        self.axis.tick_params(axis='both', which='major', labelsize=lbfontsize, pad=20)
        self.axis.set_xticklabels(self.axis.get_xticks())
        self.axis.set_yticklabels(self.axis.get_yticks())
        self.axis.grid(color='k', linestyle=(0.5, [2,6]), linewidth=1.)

    # make colorbar look tolerable
    def beautify_colorbar(self, cb_label):
        txfontsize, lbfontsize = self.get_font_sizes()
        self.colorbar.set_label(cb_label, fontsize=txfontsize)
        cb_la = [ti.get_text().replace('$', '') for ti in self.colorbar.ax.get_yticklabels()]
        self.colorbar.ax.set_yticklabels(cb_la, fontsize=lbfontsize)

    # make custom tickmarks
    def make_ticks(self, **kwargs):
        # create tickmark arrays
        numxtick = 4
        numytick = 4
        if 'numxtick' in kwargs:
            numxtick = kwargs['numxtick']
        if 'numytick' in kwargs:
            numytick = kwargs['numytick']

        xticks = np.linspace(self.xbounds[0], self.xbounds[1], numxtick+1)
        yticks = np.linspace(self.ybounds[0], self.ybounds[1], numytick+1)
        print xticks

        # draw tickmarks
        self.plot.xticks(xticks)
        self.plot.yticks(yticks)
