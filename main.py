import sys
import math
import json
import carga
import run
import utills
from router import router
from host import host


if __name__ == "__main__":
  routers = carga.CreatNetwork(sys.argv[1]) #carrega os dados da rede
  utills.plotTopologia(routers)
  run.analise(routers,sys.argv[1])
  input()