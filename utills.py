import random

def gerate_xy(n_hosts,width,height):
  XY = []
  for _ in range(n_hosts):
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    XY.append((x,y))
  return XY