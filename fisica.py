import packet

# Camada Fisica
class fisica():
  '''
  @param link tuple (origin,destino)
  @param ativo boolean (true|false)
  '''
  def __init__(self,link):
    self.__link = link #link é uma tupla com (origin,destino)
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