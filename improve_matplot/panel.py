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
        self.txscale = 18./1000.
        self.lbscale = 14./1000.
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
        lpix = np.min(fpix)

        txfontsize = lpix*self.txscale
        lbfontsize = lpix*self.lbscale
        return txfontsize, lbfontsize

    # make axis look tolerable
    def beautify_axis(self, plt_title, xlabel, ylabel, nogrid):
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
        xtlabels = ['{:.2f}'.format(xtl) for xtl in self.axis.get_xticks()]
        ytlabels = ['{:.2f}'.format(ytl) for ytl in self.axis.get_yticks()]
        print xtlabels, ytlabels
        self.axis.set_xticklabels(xtlabels)
        self.axis.set_yticklabels(ytlabels)
        self.axis.grid(color='k', linestyle=(0.5, [2,6]), linewidth=1.)
        if nogrid:
            self.axis.grid()

    # make colorbar look tolerable
    def beautify_colorbar(self, cb_label):
        txfontsize, lbfontsize = self.get_font_sizes()
        self.colorbar.set_label(cb_label, fontsize=txfontsize)
        cb_la = [ti.get_text().replace('$', '') for ti in self.colorbar.ax.get_yticklabels()]
        self.colorbar.ax.set_yticklabels(cb_la, fontsize=lbfontsize)

    # make custom tickmarks
    def make_ticks(self, numxtick, numytick):
        # create tickmark arrays
        xticks = np.linspace(self.xbounds[0], self.xbounds[1], numxtick)
        yticks = np.linspace(self.ybounds[0], self.ybounds[1], numytick)

        # draw tickmarks
        self.axis.xaxis.set_ticks(xticks)
        self.axis.yaxis.set_ticks(yticks)

    # method to tie individual style methods together
    def beautify_panel(self, **kwargs):
        # set defaults
        numxtick = 4
        numytick = 5
        plt_title = ''
        xlabel = ''
        ylabel = ''
        cblabel = ''
        nogrid = False

        # check for different values in kwargs
        if 'numxtick' in kwargs:
            numxtick = kwargs['numxtick']
        if 'numytick' in kwargs:
            numytick = kwargs['numytick']
        if 'plt_title' in kwargs:
            plt_title = kwargs['plt_title']
        if 'xlabel' in kwargs:
            xlabel = kwargs['xlabel']
        if 'ylabel' in kwargs:
            ylabel = kwargs['ylabel']
        if 'cblabel' in kwargs:
            cblabel = kwargs['cblabel']
        if 'nogrid' in kwargs:
            nogrid = kwargs['nogrid']

        # call functions to improve panel
        self.make_ticks(numxtick, numytick)
        self.beautify_axis(plt_title, xlabel, ylabel, nogrid)
        self.beautify_colorbar(cblabel)
        self.plot.tight_layout()
