import utills
import host 
import router

def plot(host.coordinates, 10, 10):

	#dimensao x e y varia de 0 a 10
	plt.axis([0,10,0,10])

	#label
	plt.xlabel("Metros")
	plt.ylabel("Metros")

	for host in router.hostlist: 
		plt.plot(host.coordinates[0], host.coordinates[1], 'ro') #(x,y, circlered)

		area = math.pi * (host.alcance**2)
		plt.scatter(host.coordinates[0], host.coordinates[1], s=area*250, alpha=1) #opaco

  for i in range(len())




	plt.show()