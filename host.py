
# import packet
from redes import redes
class host(redes):
	# ID = 0

	def __init__(self, ID_router,ID, position,energy,reach):
		super().__init__()
		# super().__init__(link)

		# self.packet = packet.packet()


	def __init__(self, ID_router,ID, xy,link, alcance):
		super().__init__(link)


		self.ID = ID #ID do host
		self.ID_router = ID_router
		self.energy = energy
		self.coordinates = position #tuple
		print("host "+ID+" criado")
		self.reach = reach 


	# def Hellou(self, topologia):
	#  return self

		self.coordinates = xy #tuple
		self.alcance = alcance #gerar range aleatoriamente




