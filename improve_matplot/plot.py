import matplotlib as mpl
mpl.use('Agg')

# use helvetica instead of default font
def adjust_fonts(mpl):
    mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    mpl.rc('text', usetex=True)
    return
