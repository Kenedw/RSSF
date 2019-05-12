
# import packet
import redes
class host(redes.redes):
	# ID = 0
	def __init__(self, ID_router,ID, xy,link):
		super().__init__(link)
		self.ID = ID #ID do host
		self.ID_router = ID_router
		# self.packet = packet.packet()
		self.coordinates = xy #tuple


