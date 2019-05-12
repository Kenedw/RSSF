
class packet():
	ID = 0
	def __init__(self, origem, destino, dado):
		packet.ID += 1

		self.ID = packet.ID
		self.dado = dado
		self.origin = origem
		self.destination = destino