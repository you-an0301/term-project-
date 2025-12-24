import math
import numpy as np
from scipy import constants as const
import matplotlib.pyplot as plt
import keys
import functions as fun
import plotfuc as plf

#1.confirm the dim the user wants to chose
d=int(input('you may chose the dimention first(from2~4):'))
if d==2:
    #2.ask for the function user want to use
    N=input(('chose a type of function(1 for polynomial,2 for Trigonometric function,3 forexponential function,4 for log function):'))
    fname=keys.get2D_keys(N)
    print('you chose the',fname,end=' ')
    fn=keys.get2D_keys2(N)
    func=getattr(fun,fn)
    name=func()
    xinit=float(input('you may enter the range of variable x now,here is the initial value:'))
    xfinal=float(input('you may enter the range of variable x now,here is the final value:'))
    x=np.arange(xinit,xfinal,1e-2)
    plf.Dim2plot_func(fname,x,name)
    print('thanks for using!')
elif d==3:
    #2.ask for the function user want to use
    N=input(('chose a type of function(1 for gravity function,2 for van der waal(CO2)(x for V,y for T),3 for wave function(x for x,y for t),4 for a bowl plot, 5 for a upper cone,6 for a below cone):'))
    fname=keys.get3D_keys(N)
    print('you chose the',fname,end=' ')
    fn=keys.get3D_keys2(N)
    func=getattr(fun,fn)
    name=func()
    xinit=float(input('you may enter the range of variable x now,here is the initial value:'))
    xfinal=float(input('you may enter the range of variable x now,here is the final value:'))
    yinit=float(input('you may enter the range of variable y now,here is the initial value:'))
    yfinal=float(input('you may enter the range of variable y now,here is the final value:'))
    len=int(input('you may enter the len for variable for np linspace:'))
    x=np.linspace(xinit,xfinal,len)
    y=np.linspace(yinit,yfinal,len)
    plf.Dim3plot_func(fname,x,y,name)
    #ask whether user wants to see the cross-sectional view
    slice_plot=int(input('Do you want to see the cross-sectional view? if yes enter 1,if not,enter 2:'))
    if slice_plot==2:
        print('thanks for using!')
    elif slice_plot==1:
        plf.Dim3sliceplot_func(fname,x,y,name)
        print('thanks for using!')
elif d==4:
    print('you chose the 4D function,and there is only gravity function.')
    xinit=float(input('you may enter the range of variable x now,here is the initial value:'))
    xfinal=float(input('you may enter the range of variable x now,here is the final value:'))
    yinit=float(input('you may enter the range of variable y now,here is the initial value:'))
    yfinal=float(input('you may enter the range of variable y now,here is the final value:'))
    len=int(input('you may enter the len for variable for np linspace:'))
    x=np.linspace(xinit,xfinal,len)
    y=np.linspace(yinit,yfinal,len)
    print('we will use the corss-sectional view to show you(you will have 3 slices of the gravity function plot):')
    plf.Dim4plot_func(x,y)
    print('thanks for using!')