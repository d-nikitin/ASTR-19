# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:10:20 2022

@author: Dima
"""

import numpy as np
from math import pi, sin

def main():
    arr = np.linspace(0, 2*pi, 1000)
    for x in arr:
        print('x = ' ,x ,' sin(x) = ', sin(x))
if __name__ == "__main__":
    main()