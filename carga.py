import json
import sys
import utills
from router import router
from host import host


def CreatNetwork(argv):
  F = open("JSON/"+argv,"r")
  data = json.loads(F.read())
  for i in data["routers"]: #roda em cada roteador
    station = router(i["id"],10)
    HostsLocatios = utills.gerate_xy(len(i["hosts"]),i["width"],i["height"])
    for index,j in enumerate(i["hosts"]): #roda em cada host
      station.insertHost(host(i["id"],j["id"],HostsLocatios[index],j["energy"],j["range"]))
    station.hostList[0].Hellou(station.hostList)
