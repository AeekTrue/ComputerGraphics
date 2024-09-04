from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
from colors import *
from dataclasses import dataclass

W = H = 400
bg = gray200
vp = np.full((H, W, 3), bg, dtype='uint8')


plt.axis('off')
plt.imshow(vp)
plt.show()
