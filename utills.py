import random
import math

def gerate_xy(n_hosts,width,height):
  XY = []
  for _ in range(n_hosts):
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    XY.append((x,y))
  return XY

def dist_euclidiana(posi):
  dim, soma = len(posi), 0
  for i in range(dim):
    soma += math.pow(posi[0][i] - posi[1][0], 2)
  return int(math.sqrt(soma))
