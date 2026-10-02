# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:22:25 2026

@author: Awais
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('student-mat.csv', sep=';')

Q1 = df['absences'].quantile(0.25)
Q3 = df['absences'].quantile(0.75)

IQR = Q3 - Q1
outliers = df[(df['absences'] < (Q1 - 1.5 * IQR)) | (df['absences'] > (Q3 + 1.5 * IQR))]
