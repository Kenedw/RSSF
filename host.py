import utills
# import packet
from redes import redes
class host(redes):
	# ID = 0
	def __init__(self, ID_router,ID, position,energy,reach):
		super().__init__()
		# super().__init__(link)
		# self.packet = packet.packet()
		self.ID = ID #ID do host
		self.ID_router = ID_router
		self.__energy = energy
		self.__discharge = False
		self.coordinates = position #tuple
		self.reach = reach 
		print("[Host] "+ID+" criado")


	def __eq__(self, other):
		if not (other == self.coordinates):
			dist = utills.dist_euclidiana([self.coordinates,other])
			return (dist<=self.reach) #tirando junto a propria rede como vizinha dela mesma
		else:
			return False

	def Hellou(self, topologia):
		self._redes__Hellou(self.coordinates,topologia)

	def send(self,destination,dado): #destination é o ID do host de destino
		print("[Host] host: {}".format(self.ID))
		print("[Host] nivel de enegia: {} uE".format(self.__energy))
		if(self.CheckEnergy()): #se não descarregado
			print("[Host] Vizinhos:",end="")
			self.PrintNeighbors()
			self.__energy -= 1
			if(self.ID==destination): #verifica se o dado é para min
				print("[Host] Dado recebido")
				self._enlace__SetDado(dado)
				print("--------FIM-------------")
			else: #se não, tenta fazer o envio
				print("[Host] Enviando para {}\n---------------".format(destination))
				self._redes__send(destination,dado)

	def CheckEnergy(self):#retorna True se carregado
		if (self.__energy<=0):
			self.__discharge = True
		return(not self.__discharge)

	#def vizinhos(self, redes.neighbors)




