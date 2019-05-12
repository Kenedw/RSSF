
# import packet
from redes import redes
class host(redes):
	# ID = 0
	def __init__(self, ID_router,ID, xy):
		super().__init__()
		# super().__init__(link)
		self.ID = ID #ID do host
		self.ID_router = ID_router
		self.energia = energia
		# self.packet = packet.packet()
		self.coordinates = xy #tuple
		print("host "+ID+" criado")


