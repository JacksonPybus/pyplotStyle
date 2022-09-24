import ROOT
import numpy as np

def getListOfNames(f):
    return [i.GetName() for i in f.GetListOfKeys()]

def getListOfObjects(f):
    return [i.ReadObj() for i in f.GetListOfKeys()]

def getLibOfObjects(f):
    return {i.GetName():i.ReadObj() for i in f.GetListOfKeys() for i in f.GetListOfKeys()}

def getData(g):
    try:
        g = ROOT.TGraphAsymmErrors(g)
    except:
        try:
            g = ROOT.TGraphErrors(g)
        except TypeError:
            print("Wrong object type")
            
    x = np.array(g.GetX())
    y = np.array(g.GetY())
    xerrh = []
    xerrl = []
    yerrh = []
    yerrl = []
    for i in range(g.GetN()):
        xerrh.append(g.GetErrorXhigh(i))
        xerrl.append(g.GetErrorXlow(i))
        yerrh.append(g.GetErrorYhigh(i))
        yerrl.append(g.GetErrorYlow(i))
    xerr = np.array((xerrl,xerrh))
    yerr = np.array((yerrl,yerrh))

    return x, y, xerr, yerr

def getData2D(h,kill_zeros=False):
    x = []
    y = []
    z = []
    xerr = []
    yerr = []
    zerr = []
    
    Nx = h.GetNbinsX()
    Ny = h.GetNbinsY()
    
    left = h.GetXaxis().GetBinLowEdge(1)
    right = h.GetXaxis().GetBinUpEdge(Nx)
    bottom = h.GetYaxis().GetBinLowEdge(1)
    top = h.GetYaxis().GetBinUpEdge(Ny)
    
    for j in range(Nx):
        x.append(h.GetXaxis().GetBinCenter(j+1))
        xerr.append(h.GetXaxis().GetBinWidth(j+1)/2.)
    
    for i in range(Ny):
        y.append(h.GetYaxis().GetBinCenter(i+1))
        yerr.append(h.GetYaxis().GetBinWidth(i+1)/2.)
        zcol = []
        zerrcol = []
        for j in range(Nx):
            zval = h.GetBinContent(j+1,i+1)
            if (kill_zeros and zval==0):
                zval = np.nan
            zcol.append(zval)
            zerrcol.append(h.GetBinError(j+1,i+1))
        z.append(zcol)
        zerr.append(zerrcol)
    
    return x, y, z, xerr, yerr, zerr, (left, right, bottom, top)
