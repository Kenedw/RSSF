import json
import sys
import utills
from router import router
from host import host
import matplotlib.pyplot as plt
import math

altura = 50
largura =50


def CreatNetwork(argv):
  data = utills.parseJson(argv)
  routerList = [] #lista de roteadores
  for i in data["routers"]: #roda em cada roteador
    station = router(i["id"],10) #instancia um roteador
    HostsLocatios = utills.gerate_xy(len(i["hosts"]),i["width"],i["height"])
    for index,j in enumerate(i["hosts"]): #roda em cada host
      station.insertHost(host(i["id"],j["id"],HostsLocatios[index],j["energy"],j["range"]))
    routerList.append(station)
#INICIO PLOT
  plt.axis([0, largura, 0, altura]) #dimensao x e y varia de 0 a 20	
  plt.xlabel("Metros")
  plt.ylabel("Metros")  

  ID=1
  for aux in HostsLocatios:
    x,y = aux[0], aux[1]
    plt.plot( x, y, 'ro') 					 #(x,y, circlered)
    plt.annotate(ID,(x,y))					 #nome aos pontos, coloca H na frente do ID
    ID +=1
    area = math.pi * (10**2)				 
    plt.scatter(x, y, s=area*50, alpha=0.1)  #opaco, desenha a area sobre o host
    
  #for aux2 in routerList					 # pecorre o vetor com todos os nos, e liga as retas
    #z,w = aux2[0], aux2[1]

    #dz = routerList[i+1]z - routerList[i].z
    #dw = routerList[i+1]w - routerList[i].w

    #plt.arrow(z, w, dz, dw)

  plt.show()
#FIM PLOT
  return routerList

