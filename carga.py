import json
import sys
import utills
from router import router
from host import host


def CreatNetwork(argv):
  F = open("JSON/"+argv,"r")
  data = json.loads(F.read())
  for i in data["routers"]:
    station = router(i["id"],10)
    HostsLocatios = utills.gerate_xy(len(i["hosts"]),10,10)
    for index,j in enumerate(i["hosts"]):
      station.insertHost(host(i["id"],j["id"],HostsLocatios[index],j["energy"]))
      print(json.dumps(j))
