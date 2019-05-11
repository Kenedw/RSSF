import json
import sys

def ImportJson(argv):
  F = open("JSON/"+argv,"r")
  data = json.loads(F.read())
  for i in data["routers"]:
    print(json.dumps(i))