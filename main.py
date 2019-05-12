import sys
import json
import carga
# import plot
import run
import router

if __name__ == "__main__":
  routers = carga.CreatNetwork(sys.argv[1]) #carrega os dados da rede
  run.analise(routers,sys.argv[1]) 


  plot.map(router.hostlist, routers ,10 ,10 )

 