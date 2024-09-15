# %%
from logging import FileHandler
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
from colors import *
from dataclasses import dataclass

OUTLINE = 1
FILL = 2

W = H = 400
bg = (0, 200, 0)
x, y = np.meshgrid(np.arange(H), np.arange(W-1, -1, -1))
width = 5


def rndm_color():
    clr = bg
    while np.all(clr == bg):
        clr = random_color()
    return clr


def draw_frame(vp, width, color):
    vp[:, :width] = color
    vp[:width, :] = color
    vp[:, -width:] = color
    vp[-width:, :] = color
    mask[:, :width] = True
    mask[:width, :] = True
    mask[:, -width:] = True
    mask[-width:, :] = True


def is_free(pixels, bg):
    return not np.any(mask[pixels])

def parabola(x, y):
    """
    return outline and fill of parabola segment
    """
    x0 = randint(width, W - width - 1)
    y0 = randint(width, H - width - 1)
    h = randint(25, 100)
    k = np.random.random() ** 2 / 2 + 0.2
    # s = -1
    s = 1 - 2 * (np.random.random() > 0.5)
    d = np.random.random() > 0.5
    if d:
        x, y = y, x

    parab = s*k * (x - x0) ** 2 + y0
    inner_parab = s * k * 1.5 * (x - x0) ** 2 + (y0 + s * width)
    line = y0 + s*h
    inner_line = y0 + s * (h - width)
    return ((s*parab < s*y) & (s*line > s*y) ), ((s*inner_parab < s*y) & (s * inner_line > s*y))
# %%
vp = np.full((H, W, 3), bg, dtype='uint8')
mask = np.full((H, W), False, dtype=bool)
draw_frame(vp, width, red)

#vp[(y > 0.01*(x - 100)**2 + 100) & (y < 200)] = green
mode = FILL | OUTLINE
cnt = 0
i = 0
MAX_ITERS = 1000
COUNT = 30
while cnt < COUNT and i < MAX_ITERS:
    outline, fill = parabola(x, y)
    if is_free(outline | fill , bg):
        cnt += 1
        if mode == (OUTLINE | FILL):
            clr = rndm_color()
            vp[outline] = black
            vp[fill] = clr
        elif mode == FILL:
            clr = rndm_color()
            vp[fill | outline] = clr
        elif mode == OUTLINE:
            vp[outline ^ fill] = black
        else:
            raise ValueError('wrong mode' ,mode)

        mask[fill | outline] = True

    i += 1

print(cnt)
plt.axis('off')
plt.imshow(vp)
plt.show()
