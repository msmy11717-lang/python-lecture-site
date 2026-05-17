import math
import matplotlib.pyplot as plt
"import japanize_matplotlib"
from matplotlib import animation

"地球"
"T[day] r[km]"
t1 = 1.
T1 = 365
r1 = 149.6*10**6

"水星"
T2 = 88
r2 = 57.9*10**6

"金星"
T3 = 224.7
r3 = 108.2*10**6

"火星"
T4 = 687.
r4 = 228*10**6

"木星"
T5 = 4331.
r5 = 778.5*10**6

"土星"
T6 = 10747.
r6 = 1432.*10**6

x0 = []
y0 = []

x2 = []
y2 = []

x3 = []
y3 = []

x4 = []
y4 = []

x5 = []
y5 = []

x6 = []
y6 = []

x2_2 = []
y2_2 = []

x3_2 = []
y3_2 = []

x4_2 = []
y4_2 = []

x5_2 = []
y5_2 = []

x6_2 = []
y6_2 = []

print(math.cos(math.pi))
for t in [t/1 for t in range(365*10)]:
    if t< 1:
        print(t)
    
    #自転あり
    x2_i = math.cos((t/t1)*2*math.pi) * (r2*math.cos((t/T2)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.sin((t/t1)*2*math.pi) * (r2*math.sin((t/T2)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    y2_i = - math.sin((t/t1)*2*math.pi) * (r2*math.cos((t/T2)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.cos((t/t1)*2*math.pi) * (r2*math.sin((t/T2)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    x2.append(x2_i)
    y2.append(y2_i)

    x3_i = math.cos((t/t1)*2*math.pi) * (r3*math.cos((t/T3)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.sin((t/t1)*2*math.pi) * (r3*math.sin((t/T3)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    y3_i = - math.sin((t/t1)*2*math.pi) * (r3*math.cos((t/T3)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.cos((t/t1)*2*math.pi) * (r3*math.sin((t/T3)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    x3.append(x3_i)
    y3.append(y3_i)

    x4_i = math.cos((t/t1)*2*math.pi) * (r4*math.cos((t/T4)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.sin((t/t1)*2*math.pi) * (r4*math.sin((t/T4)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    y4_i = - math.sin((t/t1)*2*math.pi) * (r4*math.cos((t/T4)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.cos((t/t1)*2*math.pi) * (r4*math.sin((t/T4)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    x4.append(x4_i)
    y4.append(y4_i)

    x5_i = math.cos((t/t1)*2*math.pi) * (r5*math.cos((t/T5)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.sin((t/t1)*2*math.pi) * (r5*math.sin((t/T5)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    y5_i = - math.sin((t/t1)*2*math.pi) * (r5*math.cos((t/T5)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.cos((t/t1)*2*math.pi) * (r5*math.sin((t/T5)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    x5.append(x5_i)
    y5.append(y5_i)

    x6_i = math.cos((t/t1)*2*math.pi) * (r6*math.cos((t/T6)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.sin((t/t1)*2*math.pi) * (r6*math.sin((t/T6)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    y6_i = - math.sin((t/t1)*2*math.pi) * (r6*math.cos((t/T6)*2*math.pi) - r1*math.cos((t/T1)*2*math.pi)) + math.cos((t/t1)*2*math.pi) * (r6*math.sin((t/T6)*2*math.pi) - r1*math.sin((t/T1)*2*math.pi))
    x6.append(x6_i)
    y6.append(y6_i)
    
    #自転なし
    x2_j = r2*math.cos((t/T2)*2*math.pi)-r1*math.cos((t/T1)*2*math.pi)
    y2_j = r2*math.sin((t/T2)*2*math.pi)-r1*math.sin((t/T1)*2*math.pi)
    x2_2.append(x2_j)
    y2_2.append(y2_j)

    x3_j = r3*math.cos((t/T3)*2*math.pi)-r1*math.cos((t/T1)*2*math.pi)
    y3_j = r3*math.sin((t/T3)*2*math.pi)-r1*math.sin((t/T1)*2*math.pi)
    x3_2.append(x3_j)
    y3_2.append(y3_j)

    x4_j = r4*math.cos((t/T4)*2*math.pi)-r1*math.cos((t/T1)*2*math.pi)
    y4_j = r4*math.sin((t/T4)*2*math.pi)-r1*math.sin((t/T1)*2*math.pi)
    x4_2.append(x4_j)
    y4_2.append(y4_j)

    x5_j = r5*math.cos((t/T5)*2*math.pi)-r1*math.cos((t/T1)*2*math.pi)
    y5_j = r5*math.sin((t/T5)*2*math.pi)-r1*math.sin((t/T1)*2*math.pi)
    x5_2.append(x5_j)
    y5_2.append(y5_j)

    x6_j = r6*math.cos((t/T6)*2*math.pi)-r1*math.cos((t/T1)*2*math.pi)
    y6_j = r6*math.sin((t/T6)*2*math.pi)-r1*math.sin((t/T1)*2*math.pi)
    x6_2.append(x6_j)
    y6_2.append(y6_j)


#グラフの体裁を整える
plt.rcParams['figure.figsize'] = (6,5)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

#枠線の太さを指定する関数
def axes_set_linewidth(axes, t=1, b=1, r=1, l=1):
    axes.spines['top'].set_linewidth(t)
    axes.spines['bottom'].set_linewidth(b)
    axes.spines['right'].set_linewidth(r)
    axes.spines['left'].set_linewidth(l)


# #変数設定
N = 100

fig, ax = plt.subplots()

ax.plot(x2_2, y2_2, color = 'blue', label = 'Mercury')  #自転なし
ax.plot(x3_2, y3_2, color = 'red', label = 'Venus')  #自転なし
ax.plot(x4_2, y4_2, color = 'orange', label = 'Mars')  #自転なし
#ax.plot(x5_2, y5_2, color = 'green', label = 'Jupiter')  #自転なし
#ax.plot(x6_2, y6_2, color = 'yellow', label = 'Saturn')  #自転なし
#ax.plot(x4, y4, color = 'red', label = 'Mars')  #自転あり

axes_set_linewidth(ax, t=0, r=0, b=2, l=2)
ax.set_xlabel('x')
ax.set_ylabel('y')
#ax.set_ylim(-1.2, 1.4)
ax.legend(frameon = False)
plt.show()
#plt.show()
#plt.subplots_adjust(top=0.9, bottom=0.2, right=0.9, left=0.2)


ims = []  #ここに1ステップごとのグラフを格納
for i in range(N):
    p = ax.plot(x2_2[i], y2_2[i], color = 'darkblue', marker = 'o', markersize = 10)
    ims.append(p)
    
ani = animation.ArtistAnimation(fig, ims, interval=100)  #ArtistAnimationでアニメーションを作成する。
ani.save('animate2.gif', writer='imagemagick', dpi = 300)  #gifで保存
