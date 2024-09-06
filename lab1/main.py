# %%
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
from colors import *
from dataclasses import dataclass

W = H = 400
bg = (0, 200, 0)
vp = np.full((H, W, 3), bg, dtype='uint8')
x, y = np.meshgrid(np.arange(H), np.arange(W-1, -1, -1))
width = 5
vp[:, :width] = red

vp[:width, :] = red
vp[:, -width:] = red
vp[-width:, :] = red

def is_free(view_port, pixels, bg):
    return np.all(view_port[pixels] == bg)

def parabola(x, y):
    x0 = randint(width, W - width - 1)
    y0 = randint(width, H - width - 1)
    h = randint(10, 100)
    k = np.random.random() ** 2 + 0.02
    # s = -1
    s = 1 - 2 * (np.random.random() > 0.5)
    d = np.random.random() > 0.5
    if d:
        x, y = y, x
    return (s*(s*k * (x - x0) ** 2 + y0 - y) < 0) & (s *(y - (y0 + s*h)) < 0)

# %%
#vp[(y > 0.01*(x - 100)**2 + 100) & (y < 200)] = green

cnt = 0
i = 0
MAX_ITERS = 1000
COUNT = 200
while cnt < COUNT and i < MAX_ITERS:
    p = parabola(x, y)
    if is_free(vp, p, bg):
        cnt += 1
        clr = bg
        while np.all(clr == bg):
            clr = random_color()
        vp[p] = clr
    i += 1

print(cnt)
plt.axis('off')
plt.imshow(vp)
plt.show()
