
import packet
import host

class router():
	def __init__(self, host, table_router, ID, energia, N_mult_acess):
		self.host = host.host()
		self. table_router = []
		self.ID = ID
		self.energia = energia
		self.N_mult_acess = N_mult_acess