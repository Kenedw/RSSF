from enlace import enlace

class redes(enlace):
  def __init__(self):
    super().__init__()
    # super().__init__(link)
    self.neighbors = []
    self.routeTable = []

  def RouteRequest(self,topologia):
    pass

  def RouteResponse(self):
    pass

  def __Hellou(self,position,topologia):
    for i in topologia:
      if(position == i):
        self.neighbors.append(i)





