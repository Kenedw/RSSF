import utills
import host 
import router

def map(router.hostlist, lista_de_nos, 10, 10): # (lista de host, lista de nos, altura, largura)

	#dimensao x e y varia de 0 a 10
	plt.axis([0,10,0,10])

	#label
	plt.xlabel("Metros")
	plt.ylabel("Metros")

	for host in router.hostlist: 
		plt.plot(host.coordinates[0], host.coordinates[1], 'ro') #(x,y, circlered)

		plt.annotate(host.ID, (host.coordinates[0], host.coordinates[1])) #nome aos pontos

		area = math.pi * (host.alcance**2)
		plt.scatter(host.coordinates[0], host.coordinates[1], s=area*250, alpha=1) #opaco, desenha a area sobre o host

	for i in range(len(?)-1): # pecorre o vetor com todos os nos, e liga as retas
		x = lista_de_nos[i].coordinates[0] 
		y = lista_de_nos[i].coordinates[1]

		dx = lista_de_nos[i+1].coordinates[0]-lista_de_nos[i].coordinates[0] #diferença entre pontos
		dy = lista_de_nos[i+1].coordinates[1]-lista_de_nos[i].coordinates[1]

		plt.arrow(x, y, dx, dy)

	plt.show()



	

