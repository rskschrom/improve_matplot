import matplotlib as mpl
mpl.use('Agg')

# use helvetica instead of default font
def adjustFonts(mpl):
    mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    mpl.rc('text', usetex=True)
    return
