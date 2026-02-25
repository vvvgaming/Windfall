# ta=(-0.4035+
# print(ta)
# ta=(-0.4035+0.1642)/Sadd
# print(ta)
# ta=(-0.4035+0.1642)/Sadd
# print(ta)
# ta=(-0.4035+0.1642)/Sadd
# print(ta)
# ta=(-0.4035+0.1642)/Sadd
# print(ta)
# ta=(-0.4035+0.1642)/Sadd
# print(ta)
# ta=(-0.4035+0.1642)/Sadd
# print(ta)





# lower=
# upper=p+margin #置信区间上限
#
# print(lower)
# print(upper)
#
# t=0.24826*(1-0.24826)/((0.02578/1.96)**2)
# print(t)

# from scipy.stats import norm
# import numpy as np
# np.set_printoptions(suppress=True)
# from scipy.stats import t

# import sympy
# import math
# from scipy.integrate import quad

# na=122254
# acta=5148
pa=3.5312

# nb=122245
# actb=5018
pb=8.529

#add_value=(0.1289-0.1197)/0.1197
add_value=(pb-pa)/pa
print("add_value:{}".format(add_value))

Sa=3.3259
Sb=18.901

Sadd=(((pb/pa)**2)*((Sa/pa)**2+(Sb/pb)**2))**0.5
#Sadd=((pa*(1-pa)/na)+(pb*(1-pb)/nb))**0.5

print("标准差：{}".format(Sadd))

max=add_value+1.96*Sadd
min=add_value-1.96*Sadd

print("置信区间：[{0},{1}]".format(min,max))

# ta=(-0.4035+0.1642)/Sadd
# print(ta)

z_scores=add_value/Sadd

print("z_scores：{}".format(z_scores))

p_values = norm.sf(abs(z_scores))*2 #twosided

print("P值：{}".format(p_values))

# Z2=(pb-pa)/((pa*(1-pa)/na)+(pb*(1-pb)/nb))**0.5
# print(Z2)
# p2=norm.sf(abs(z_scores))*2 #twosided
# print(p2)
#
# m=(pb-pa)-1.96*((pa*(1-pa)/na)+(pb*(1-pb)/nb))**0.5
# print(m)
# m2=(pb-pa)+1.96*((pa*(1-pa)/na)+(pb*(1-pb)/nb))**0.5
# print(m2)

def func(x):
    return 1/math.sqrt(2*math.pi)*math.e**(-x**2/2)

#z=sympy.symbols('z')
#f=1/math.sqrt(2*math.pi)*math.e**(-z**2/2)
p_z,err=quad(func,z_scores,-z_scores)

print("pz:{}".format((1-p_z)))
