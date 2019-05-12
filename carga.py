import json
import sys

def CreatNetwork(argv):
  F = open("JSON/"+argv,"r")
  data = json.loads(F.read())
  for i in data["routers"]:
    print(json.dumps(i))
