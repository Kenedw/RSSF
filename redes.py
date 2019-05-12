from enlace import enlace

class redes(enlace):
  def __init__(self):
    super().__init__()
    # super().__init__(link)
    self.__neighbors = []
    self.routeTable = []
    self.__topologia = []

  def RouteRequest(self,topologia):
    pass

  def RouteResponse(self):
    pass

  def PrintNeighbors(self):
    print("{", end="")
    for i in self.__neighbors:
      print(i.ID+":", end="")
    print("}")

  def __Hellou(self,position,topologia):
    self.__topologia = topologia #guarda a topologia da rede para não precisar reenviar
    self.__neighbors = []
    for i in topologia: #i é um host
      if(i.CheckEnergy()):
        if(position == i):
          self.__neighbors.append(i)
          # print("[Redes] host {} é vizinho de {}".format(position,i.ID))
          # utills.Log("host {} é vizinho de {}".format(position,i.coordinates))

  def __send(self,destination,dado):
    sending = False #verifica se já foi enviado
    for i in self.__neighbors: #verifica se é vizinho
      if(i.ID == destination):
        if(self._enlace__GetBusy()):#se o enlace estiver ocupado, 
          print("[Redes] Canal ocupado, esperando liberação")
          while(not self._enlace__GetBusy):#espera desocupar
            pass
        if(not self._enlace__GetBusy()):#se o enlace não estiver ocupado
          self._enlace__SendDado(i,dado) #envia referencia do host e o dado
          sending = True #marca como enviado
          break
    if(not sending):
      pass





