plotdim_keys={'2':'Dim2plot_func','3':'Dim3plot_func','4':'g3Dfunc'}
Dim2fname_keys={'1':'polynomial','2':'Trigonometric','3':'expfunc','4':'logfunc'}
Dim3fname_keys={'1':'gfunc','2':'vander_forCO2','3':'wave','4':'bowl','5':'cone_1','6':'cone_2'}
Tri_keys={'1':'sinfunc','2':'cosfunc','3':'tanfunc','4':'cotfunc','5':'secfunc','6':'cscfunc'}

Dim2fname_keys2={'1':'polynomialname','2':'Trigonometric','3':'expfuncname','4':'logfuncname'}
Tri_keys2={'1':'sinfuncname','2':'cosfuncname','3':'tanfuncname','4':'cotfuncname','5':'secfuncname','6':'cscfuncname'}
Dim3fname_keys2={'1':'gfuncname','2':'vander_forCO2name','3':'wavename','4':'bowlname','5':'conename','6':'conename'}

'get 2D funcname'
def get2D_keys(N):
    if N=='2':
        M=input('please choose a function of tirgonometric function(1 for sin,2 for cos,3 for tan,4 for cot,5 for sec,6 for csc):')
        return Tri_keys[M] 
    else:
        return Dim2fname_keys[N]
'get 3D funcname'    
def get3D_keys(N):
    return Dim3fname_keys[N]
'get 2D func'
def get2D_keys2(N):
    if N=='2':
        M=input('please choose a function of tirgonometric function(1 for sin,2 for cos,3 for tan,4 for cot,5 for sec,6 for csc):')
        return Tri_keys2[M] 
    else:
        return Dim2fname_keys2[N]
'get 3D funcname'
def get3D_keys2(N):
    return Dim3fname_keys2[N]