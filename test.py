import numpy as np
import matplotlib.pyplot as plt

# f(x) = (x-1)**2
# 今　x＝2,y=1


x = 3

def f(x):
  return ((x-2)**2)

while f(x) > 0.1:
  current_x = x -0.2 *((2 * x) - 4)
  x = current_x
  print(f(x))

log = "誤差が最も小さくなる数値は{0}です".format(x)
print(log)

