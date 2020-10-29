import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

def f(t):
    return np.exp(-t)

def g(t):
    return np.exp(t)

def h(t):
    return np.exp(0*t)

t1 = np.arange(-5.0, 5.0, 0.1)
t2 = np.arange(-5.0, 5.0, 0.1)

plt.subplot(221)      # 2 rows, 2 column, 3ndplot

plt.plot(t1, f(t1), '-b',label='-a')
plt.plot(t2, g(t2), '-r',label='a')
plt.plot(t2, h(t2), 'g-',label='a=1')
#plt.legend(loc='best')

#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('t/s')
#plt.ylabel('C')
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("x(t)")

N = 500
a = np.linspace(-1.75,1.75,num=N)
# ω = t/2

fs = 0.6
fx = -0.3
x3 = 5 * np.cos(2 * math.pi * fs * a + math.pi*fx)
plt.subplot(223)
plt.plot(a,x3)
plt.title(u'x(t)=Acos(ωt+φ )')
plt.ylim(-5.0,5.0)
plt.xlabel('t/s')
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))

def I2(n):
    return np.power(-2,n)

def y2(n):
    return np.power(-1/2,n)


n2 = np.arange(-5.0, 5.0)

plt.subplot(222)      # 2 rows, 3 column, 4plot
plt.plot(n2, I2(n2), 'm', 'm-')
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-10,10))
#设置坐标轴名称
plt.xlabel('t')
#plt.ylabel('X[t]')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"x(t)")


plt.subplot(224)      # 2 rows, 3 column, 5plot
plt.plot(n2, y2(n2), 'y', 'y-')
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-10,10))
#设置坐标轴名称
plt.xlabel('t')
#plt.ylabel('X[t]')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"x(t)")

plt.show()
