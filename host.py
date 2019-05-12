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
		self.energy = energy
		self.coordinates = position #tuple
		print("host "+ID+" criado")
		self.reach = reach 


	def __eq__(self, other):
		# print(other)
		dist = utills.dist_euclidiana([self.coordinates,other])
		return (dist<self.reach) #tirando junto a propria rede como vizinha dela mesma


	def Hellou(self, topologia):
		return self._redes__Hellou(self.coordinates,topologia)




