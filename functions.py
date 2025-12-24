import numpy as np
from scipy import constants as const
import math

'polynomial'
def polynomialname():
    coeffs_num=input('please enter an anarray of coefficient and seperate it by space:')
    coeffs=list(map(float,coeffs_num.split()))
    return coeffs
def polynomial(x,name):
    return np.polyval(name,x)  

'sine'
def sinfuncname():
    A=float(input('please enter an amplitude:'))
    omega=float(input('please enter an angular frequency:'))
    phi=float(input('please enter a phase:'))
    return f'{A} * np.sin({omega} * x + {phi})'
def sinfunc(x,name):
    return eval(name,{'np':np},{'x':x})

'cosine'
def cosfuncname():
    A=float(input('please enter an amplitude:'))
    omega=float(input('please enter an angular frequency:'))
    phi=float(input('please enter a phase:'))
    return f'{A} * np.cos({omega} * x + {phi})'
def cosfunc(x,name):
    return eval(name,{'np':np},{'x':x})

'tangent'
def tanfuncname():
    A=float(input('please enter an amplitude:'))
    omega=float(input('please enter an angular frequency:'))
    phi=float(input('please enter a phase:'))
    return f'{A} * np.tan({omega} * x + {phi})'
def tanfunc(x,name):
    return eval(name,{"np": np},{'x':x})

'cotangent'
def cotfuncname():
    A=float(input('please enter an amplitude:'))
    omega=float(input('please enter an angular frequency:'))
    phi=float(input('please enter a phase:')) 
    return f'{A} * np.tan({omega} * x + {phi}+({np.pi})/{2})'
def cotfunc(x,name):
    return eval(name,{"np": np},{'x':x})

'secant'
def secfuncname():
    A=float(input('please enter an amplitude:'))
    omega=float(input('please enter an angular frequency:'))
    phi=float(input('please enter a phase:'))
    return f'{A} / np.cos({omega} * x + {phi})'
def secfunc(x,name):
    return eval(name,{"np": np},{'x':x})

'cosecant'
def cscfuncname():
    A=float(input('please enter an amplitude:'))
    omega=float(input('please enter an angular frequency:'))
    phi=float(input('please enter a phase:'))
    return f'{A} / np.sin({omega} * x + {phi})'
def cscfunc(x,name):
    return eval(name,{"np": np},{'x':x})

'exponential'
def expfuncname():
    a=float(input('please enter a base for the exponential funcrion:'))
    return f'{a}**x'
def expfunc(x,name):
    return eval(name,{'np':np},{'x':x})

'logarithmic'
def logfuncname():
    b=float(input('please enter a base for the log function,do not enter 0 and do not enter 0 in initial and final value:'))
    return f'np.log(x)/np.log({b})'
def logfunc(x,name):
    return eval(name,{'np':np},{'x':x})

'gravity'
def gfuncname():
    m=float(input('please enter the first mass:'))
    M=float(input('please enter the second mass:'))
    return f'(const.G*{m}*{M})/(x**{2}+y**{2})'
def gfunc(x,y,name):
    x,y=np.meshgrid(x,y)
    return eval(name,{'const':const,'x':x,'y':y})

'Van der Waals'
def vander_forCO2name():
    R = 8.314 
    Tc = 304 
    Pc = 73.6e5 
    a = (27 * R**2 * Tc**2) / (64 * Pc)
    b = (R * Tc) / (8 * Pc)
    return f'(({R} * T / (V - {b})) - ({a} / V**{2})) *{1e-5}'
def vander_forCO2(V,T,name):
    T,V=np.meshgrid(T,V)
    return eval(name,{'V':V},{'T':T})

'wave function'
def wavename():
    A=float(input('please enter an amplitude:'))
    omega=float(input('please enter an angular frequency:'))
    lamb=float(input('please enter a wave length:'))
    phi=float(input('please enter a phase:')) 
    k=2*np.pi/lamb
    return f'{A}*np.sin({k}*x-{omega}*t+{phi})'
def wave(x,y,name):
    x,y=np.meshgrid(x,y)
    return eval(name,{'np':np,'x':x,'t':y})

'bowl'
def bowlname():
    return f'x**{2}+y**{2}'
def bowl(x,y,name):
    x,y=np.meshgrid(x,y)
    return eval(name,{'x':x},{'y':y})

'cone'
def conename():
    return 1
def cone_1(x,y,name):
    x,y=np.meshgrid(x,y)
    return np.sqrt(x**2+y**2)
def cone_2(x,y,name):
    x,y=np.meshgrid(x,y)
    b=-np.sqrt(x**2+y**2)
    return b

