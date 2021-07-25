
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors



#sąsiedztwo Moore'a
neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))
EMPTY, TREE, FIRE = 0, 1, 2

colors_list = ["black", "green", "white", "orange"]
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3]
norm = colors.BoundaryNorm(bounds, cmap.N)

def iterate(X):

    X1 = np.zeros((ny, nx))
    for ix in range(-1,nx-1):
        for iy in range(-1,ny-1):
            if X[iy,ix] == EMPTY and np.random.random() <= p:
                X1[iy,ix] = TREE
            if X[iy, ix] == TREE:
                X1[iy,ix] = TREE
                for dx,dy in neighbourhood:
                    if abs(dx) == abs(dy) and np.random.random() <= 1:
                        continue
                    if X[iy+dy,ix+dx] == FIRE:
                        X1[iy,ix] = FIRE
                        break
                else:
                    if np.random.random() <= f:
                        X1[iy,ix] = FIRE
    return X1

#tutaj ile procent powierzchni zajmie las przy pierwotnym wygenerowaniu
forest_fraction = 0.3

# p = prawdopodobieństwo że urośnie drzewko
# f = prawdopodobieństwo że uderzy piorun
p = 0.01
f = 0.009

# las rozmiar
nx, ny = 100,100

# kratka
X  = np.zeros((ny, nx))
X[0:ny, 0:nx] = np.random.randint(0, 2, size=(ny, nx))
X[0:ny, 0:nx] = np.random.random(size=(ny, nx)) < forest_fraction

fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=norm)
fig = plt.gcf()
fig.canvas.set_window_title('Projekt z fizyki - grupa PJESKI')

def animate(i):
    im.set_data(animate.X)
    animate.X = iterate(animate.X)

animate.X = X

interval = 500
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=200)
plt.show()
