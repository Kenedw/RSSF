import utills
import host 

def plot(host.coordinates, 10, 10):

	#dimensao x e y varia de 0 a 10
	plt.axis([0,10,0,10])

	#label
	plt.xlabel("Metros")
	plt.ylabel("Metros")

	for host in host_list: 
		plt.plot(host.coordinates[0], host.coordinates[1], 'ro') #(x,y, circlered)

		area = math.pi *(host.range)

	 	




	plt.show()