import random
import math
import json
import matplotlib.pyplot as plt

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
  return abs(int(math.sqrt(soma)))

def parseJson(link):
  F = open("JSON/"+link,"r")
  return json.loads(F.read())

def plotTopologia(topologia):
  plt.xlabel("Metros")
  plt.ylabel("Metros")  
  for j in topologia:
    for i in j.hostList:
      x,y = i.coordinates
      plt.plot( x, y, 'ro')            #(x,y, circlered)
      plt.annotate(i.ID,(x,y))         
      area = math.pi * (i.reach*i.reach)    
      plt.scatter(x, y, s=area*50, alpha=0.1)  #opaco, desenha a area sobre o host
    plt.show()
