import matplotlib.pyplot as plt

def placeText(text, loc=1, ax=None, offset=8, xoffset=0, yoffset=0, **kwargs):
    if ax is None:
        ax = plt.gca()
    if (loc == 1) or (loc == 'upper right'):
        xy = (1,1)
        xytext = (-offset-xoffset,-offset-yoffset)
        ha = 'right'
        va = 'top'
    elif (loc == 2) or (loc == 'upper left'):
        xy = (0,1)
        xytext = (offset+xoffset,-offset-yoffset)
        ha = 'left'
        va = 'top'
    elif (loc == 3) or (loc == 'lower left'):
        xy = (0,0)
        xytext = (offset+xoffset,offset+yoffset)
        ha = 'left'
        va = 'bottom'
    elif (loc == 4) or (loc == 'lower right'):
        xy = (1,0)
        xytext = (-offset-xoffset,offset+yoffset)
        ha = 'right'
        va = 'bottom'
    elif (loc == 5) or (loc == 'right'):
        xy = (1,0.5)
        xytext = (offset+xoffset,yoffset)
        ha = 'left'
        va = 'center'
    elif (loc == 6) or (loc == 'center left'):
        xy = (0,0.5)
        xytext = (offset+xoffset,yoffset)
        ha = 'left'
        va = 'center'
    elif (loc == 7) or (loc == 'center right'):
        xy = (1,0.5)
        xytext = (-offset-xoffset,yoffset)
        ha = 'right'
        va = 'center'
    elif (loc == 8) or (loc == 'lower center'):
        xy = (0.5,0)
        xytext = (xoffset,offset+yoffset)
        ha = 'center'
        va = 'bottom'
    elif (loc == 9) or (loc == 'upper center'):
        xy = (0.5,1)
        xytext = (xoffset,-offset-yoffset)
        ha = 'center'
        va = 'top'
    elif (loc == 10) or (loc == 'center'):
        xy = (0.5,0.5)
        xytext = (xoffset,yoffset)
        ha = 'center'
        va = 'center'
    return ax.annotate(text, xy=xy, xytext=xytext, ha=ha, va=va, xycoords='axes fraction', textcoords='offset points', **kwargs)
