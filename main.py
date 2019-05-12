import sys
import matplotlib.pyplot as plt
import math
import json
import carga
import run
import utills
from router import router
from host import host

altura = 20
largura =20

if __name__ == "__main__":
  routers = carga.CreatNetwork(sys.argv[1]) #carrega os dados da rede
  run.analise(routers,sys.argv[1])   