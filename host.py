
# import packet
from redes import redes
class host(redes):
	# ID = 0
	def __init__(self, ID_router,ID, position,energy):
		super().__init__()
		# super().__init__(link)
		self.ID = ID #ID do host
		self.ID_router = ID_router
		self.energy = energy
		# self.packet = packet.packet()
		self.coordinates = position #tuple
		print("host "+ID+" criado")


