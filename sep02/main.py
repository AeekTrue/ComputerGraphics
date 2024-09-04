# %%

from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
from colors import *


def rect(view_port, x, y, w, h, color):
    view_port[y:y+h, x:x+w] = color

def intersect(x, y, w, h, rects):
    for r in rects:
        x1, y1, w1, h1 = r
        if not(x > x1+w1 or y > y1 + h1 or x + w < x1 or y + h < y1):
            return True
    return False


# %%
W = H = 400
bg = gray200
vp = np.full((H, W, 3), bg, dtype='uint8')


# %% Fill and borders
vp[:,:] = green

width = 5
vp[:, :width] = red
vp[:width, :] = red
vp[:, -width:] = red
vp[-width:, :] = red

# %% random rect
n = 0
i = 0
rects = []
while n < 20 and i < 1000:
    i += 1
    r_w, r_h = randint(60, 100), randint(60, 100)
    topleft_x = randint(width, W - width - 1 - r_w)
    topleft_y = randint(width, H - width - 1 - r_h)
    clr = random_color()

    if np.all(clr == bg) or intersect(topleft_x, topleft_y, r_w, r_h, rects):
        continue
    rect(vp, topleft_x, topleft_y, r_w, r_h, clr)
    rects.append((topleft_x, topleft_y, r_w, r_h))
    # print('done')
    n += 1


plt.axis('off')
plt.imshow(vp)
plt.show()
