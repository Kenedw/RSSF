import json
import utills

def analise(routerList,argv):
  data = utills.parseJson(argv)
  for flow in data["flows"]:
    for i in routerList: # i é um roteador
      if(i.ID == flow["target"]):
        #hellou para que cada host saiba quem pe seu vizinho 
        for j in i: # j é um host do roteador i
          j.Hellou(i.hostList)
        #envio da msg do test flow
        for j in i:
          pass
        
        break
