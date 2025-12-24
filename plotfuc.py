import numpy as np
import matplotlib.pyplot as plt
import functions as fun
from scipy import constants as const

'average'
def avg(x,fname,name,h=1e-2):
    sum=0.0
    func=getattr(fun,fname)
    for i in range(len(x)):
        sum+=h*func(x[i],name)
    avg=sum/x[-1]-x[0]
    if abs(avg)>=1e10:
        return 'inf'
    else:
        return avg
    
'2D plot'
def Dim2plot_func(fname,x,name):
    func=getattr(fun,fname)
    y=func(x,name)
    plt.xlabel('x(axis)') 
    plt.ylabel('y(axis)')
    plt.title(f'{fname},func plot')
    average=f'the average of the function is {avg(x,fname,name,h=1e-5):.4f}'
    plt.plot(x,y,label=average)
    plt.axis([x[0],x[-1],-10,10])
    plt.grid(True)
    plt.legend()
    plt.show()

'3D plot'
def Dim3plot_func(fname,x,y,name):
    func=getattr(fun,fname)
    z=func(x,y,name)
    x,y=np.meshgrid(x,y)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],projection='3d')
    surf=ax.plot_surface(x,y,z, cmap='viridis', edgecolor='k', linewidth=0.5, alpha=0.5)
    ax.set_xlabel('x(axis)') 
    ax.set_ylabel('y(axis)')
    ax.set_zlabel('z(axis)')
    ax.set_title(f'{fname},function plot')
    plt.show()

'slice'
def Dim3sliceplot_func(fname,x,y,name):
    c=input('chose an axis you want to hold constant(x,y):')
    func=getattr(fun,fname)
    z=func(x,y,name)
    if c=='x':
        x0=float(input('enter the constant:'))
        j = np.argmin(np.abs(x-x0))
        y_slice = y   
        z_slice = z[:,j]
        plt.figure(figsize=(6, 4))
        plt.plot(y_slice, z_slice)
        plt.xlabel('y')
        plt.ylabel('z')
        plt.title(f'Cross-section of z = {fname} at x = {x0}')
        plt.grid(True)
        plt.show()  
    elif c=='y':
        y0=float(input('enter the constant:'))
        j = np.argmin(np.abs(y-y0))
        x_slice = x   
        z_slice = z[j, :]
        plt.figure(figsize=(6, 4))
        plt.plot(x_slice, z_slice)
        plt.xlabel('x')
        plt.ylabel('z')
        plt.title(f'Cross-section of z = {fname} at y = {y0}')
        plt.grid(True)
        plt.show()  
    
'4D plot'
def Dim4plot_func(x,y):
    m=float(input('please enter the first mass:'))
    M=float(input('please enter the second mass:'))
    a=float(input('please chose a height for the slices of gravity force plot:'))
    b=float(input('please chose another height for the slices of gravity force plot:'))
    c=float(input('please chose another height for the slices of gravity force plot:'))
    z_slices = [a, b, c]
    x,y=np.meshgrid(x,y)
    fig, axes = plt.subplots(1, len(z_slices), figsize=(5*len(z_slices), 5))
    if len(z_slices) == 1:
        axes = [axes]
    last_cs = None

    for ax, z0 in zip(axes, z_slices):
        R2 = x**2 + y**2 + z0**2
        R2[R2 == 0] = np.nan

        g = const.G * M *m/ R2
        logg = np.log10(g)

        cs = ax.contourf(x, y, logg, levels=20, cmap='plasma')
        last_cs = cs

        ax.scatter(0, 0, color='k', s=20)
        ax.set_aspect('equal', 'box')
        ax.set_title(f'z = {z0}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
    fig.subplots_adjust(right=0.88)   
    cbar_ax = fig.add_axes([0.90, 0.15, 0.02, 0.7])     
    fig.colorbar(last_cs, cax=cbar_ax, label='log10(|g|)')
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 或 'SimHei', 'PMingLiU' 等支援中文的字型
    plt.rcParams['axes.unicode_minus'] = False  
    plt.suptitle('3D重力場的等高線切片')
    plt.show()