import numpy as np
import matplotlib.pyplot as plt

def plotPoints(x,y,xerr=None,yerr=None,ls='',fmt='.',**kwargs):
    """Plot y versus x as markers with attached errorbars. Does not include connecting lines by default.

    Parameters
    ----------
    x, y : The data positions.
    
    xerr, yerr : The errorbar sizes.
    """
    return plt.errorbar(x,y,xerr=xerr,yerr=yerr,ls=ls,fmt=fmt,**kwargs)

def plotBand(x,y,yerr=None,label=None,alpha=0.25,**kwargs):
    """Plot y versus x as markers with attached errorband.

    Parameters
    ----------
    x, y : The data positions.
    
    yerr : The errorbar size.
    """
    line = plt.plot(x,y,**kwargs)[0]
    band = plt.fill_between(x,np.array(y)-np.array(yerr[0]),np.array(y)+np.array(yerr[1]),color=line.get_color(),alpha=alpha,zorder=line.zorder,label=label)
    return line, band
