#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:01:38 2026

@author: awais
"""

import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt

img = skio.imread("freq.tif")
plt.figure()
plt.imshow(img, cmap='gray')

enhanced = np.log(1+img)
plt.figure()
plt.imshow(enhanced, cmap = 'gray')

