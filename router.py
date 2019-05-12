
# from packet import packet
from host import host

class router():
	# ID=0
	def __init__(self, ID, sizeQueue):
		self.__ID = ID
		self.TableRouter = []
		self.sizeQueue = sizeQueue
		self.hostList = []

	def insertHost(self,Host):
		self.hostList.append(Host)