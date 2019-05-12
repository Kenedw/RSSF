
# from packet import packet
from host import host

class router():
	# ID=0
	def __init__(self, ID, sizeQueue):
		self.ID = ID
		self.TableRouter = []
		self.sizeQueue = sizeQueue
		self.hostList = []

	def insertHost(self,Host):
		self.hostList.append(Host)

	def AllHellou(self):
		#hellou para que cada host saiba quem pe seu vizinho 
		for i in self.hostList: # i é um host do roteador
			i.Hellou(self.hostList)
