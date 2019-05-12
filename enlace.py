import fisica

class enlace(fisica.fisica):
  def __init__(self):
    super().__init__()
    # super.__init__(link)
    # self.__busy = self._fisica__GetAtivo()

  def __GetDado(self):
    return self._fisica__GetDado

  def __SetDado(self,dado):
    self._fisica__SetDado = dado

  def __GetBusy(self):
    # return self.__busy
    # self.__SetBusy(not )
    return self._fisica__GetAtivo()

  def __SetBusy(self,busy):
    # self.__busy = busy
    self._fisica__SetAtivo(busy)

  def __SendDado(self,hostDest,dado):
    self._enlace__SetBusy(True)
    self._fisica__SetDado(dado)
    self._fisica__SendDado(hostDest)
    self._enlace__SetBusy(False)
