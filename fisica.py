from packet import packet

# Camada Fisica
class fisica():
  '''
  @param link list(hosts)
  @param ativo boolean (true|false)
  '''
  def __init__(self):
    self.__link = [] 
    # self.__link = link 
    self.__is_ativo = False
    self.__dado = packet

  def __SetAtivo(self,ativo):
    self.__is_ativo = ativo

  def __GetAtivo(self):
    return self.__is_ativo

  def __SetDado(self,dado):
    self.__dado = dado

  def __GetDado(self):
    return self.__dado

  def __SendDado(self,hostDest):
    hostDest.send(hostDest.ID,self.__GetDado())
