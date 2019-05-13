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
  soma = math.pow(posi[0][0] - posi[1][0], 2)
  soma += math.pow(posi[0][1] - posi[1][1], 2)
  return int(math.sqrt(soma))

def parseJson(link):
  F = open("JSON/"+link,"r")
  return json.loads(F.read())

def plotTopologia(topologia):
  plt.xlabel("Metros")
  plt.ylabel("Metros")  
  for j in topologia:
    for i in j.hostList:
      # print(f"{i.ID} na coordenada:{i.coordinates}")
      x,y = i.coordinates
      plt.plot( x, y, 'bo')            #(x,y, circlered)
      plt.annotate(i.ID,(x,y))         
      area = math.pi * (i.reach*i.reach)    
      plt.scatter(x, y, s=area*i.reach*math.pi, alpha=0.1)  #opaco, desenha a area sobre o host
    plt.show(block=False)
