# -*- coding: latin-1 -*-
"""
Created on Wed Jul 27 20:19:31 2011

@author: antoanne
"""

from numpy import loadtxt
from matplotlib.pyplot import plot, scatter, boxplot, show, title, legend, figure
from scipy import linspace, polyval, polyfit, sqrt, stats, randn, array
from scipy.stats import describe, cumfreq
from scipy.stats.kde import gaussian_kde
from pylab import hist

datapath = "/home/antoanne/Dropbox/Work-2011/Mestrado/Modelagem/maternidade/"
dataset = "partosDia.csv"

data = loadtxt(datapath+dataset, delimiter=',', skiprows = 1, converters = {0: datestr2num})

header = {'data':0,
        'atendimento':1,
        'admissao':2,
        'alta':3,
        'pc':4,
        'pn':5,
        'wc':6,
        'transf':7,
        'lua':8,
        }

plot(data[:,header['data']], data[:,header['atendimento']], 'y', label='Atendimentos')
plot(data[:,header['data']], data[:,header['admissao']], 'm', label='Admissoes')
plot(data[:,header['data']], data[:,header['alta']], 'g', label='Altas')
plot(data[:,header['data']], data[:,header['pc']], 'b', label='PC', linewidth=2)
plot(data[:,header['data']], data[:,header['pn']], 'c', label='PN', linewidth=2)
plot(data[:,header['data']], data[:,header['wc']], 'r', label='WC')
plot(data[:,header['data']], data[:,header['transf']], 'k', label='Transferencias')
plot(data[:,header['data']], data[:,header['pc']]+data[:,header['pn']], 'b', label='Partos', linewidth=2)
plot(data[:,header['data']], data[:,header['lua']], '*k', label='Lua', linewidth=2)

legend()
figure(2)