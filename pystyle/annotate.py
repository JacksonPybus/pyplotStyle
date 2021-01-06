import matplotlib.pyplot as plt

def placeText(text, loc=1, ax=None, offset=8, **kwargs):
    if ax is None:
        ax = plt.gca()
    if (loc == 1) or (loc == 'upper right'):
        xy = (1,1)
        xytext = (-offset,-offset)
        ha = 'right'
        va = 'top'
    elif (loc == 2) or (loc == 'upper left'):
        xy = (0,1)
        xytext = (offset,-offset)
        ha = 'left'
        va = 'top'
    elif (loc == 3) or (loc == 'lower left'):
        xy = (0,0)
        xytext = (offset,offset)
        ha = 'left'
        va = 'bottom'
    elif (loc == 4) or (loc == 'lower right'):
        xy = (1,0)
        xytext = (-offset,offset)
        ha = 'right'
        va = 'bottom'
    elif (loc == 5) or (loc == 'right'):
        xy = (1,0.5)
        xytext = (offset,0)
        ha = 'left'
        va = 'center'
    elif (loc == 6) or (loc == 'center left'):
        xy = (0,0.5)
        xytext = (offset,0)
        ha = 'left'
        va = 'center'
    elif (loc == 7) or (loc == 'center right'):
        xy = (1,0.5)
        xytext = (-offset,0)
        ha = 'right'
        va = 'center'
    elif (loc == 8) or (loc == 'lower center'):
        xy = (0.5,0)
        xytext = (0,offset)
        ha = 'center'
        va = 'bottom'
    elif (loc == 9) or (loc == 'upper center'):
        xy = (0.5,1)
        xytext = (0,-offset)
        ha = 'center'
        va = 'top'
    return ax.annotate(text, xy=xy, xytext=xytext, ha=ha, va=va, xycoords='axes fraction', textcoords='offset points', **kwargs)
