import sys
import json
import carga
import plot
import run

if __name__ == "__main__":
  routers = carga.CreatNetwork(sys.argv[1])
  run.analise(routers,sys.argv[1])


