# from numba import njit
import pprint
import queue
from laberinto import Laberinto
from agente import Agente
import algoritmo
import copy

laberinto = Laberinto()
agente = Agente()
cola = queue.Queue()

agente.maxx, agente.maxy = laberinto.laberinto.shape
agente.xob, agente.yob = laberinto.fin


resp = algoritmo.generar_estados_posibles(laberinto, agente)
trabajados = []

if resp == True:
    print('se hallo solucion')
elif not resp == None:
    algoritmo.agregar_agentes_cola(cola,resp, trabajados)
else:
    print('spawneado imposible')


while not cola.empty():
    agente = cola.get()
    trabajados.append(copy.copy(agente))
    resp = algoritmo.generar_estados_posibles(laberinto, agente)
    if resp == True:
        print('se hallo solucion')
        break
    elif not resp == None:
        algoritmo.agregar_agentes_cola(cola,resp,trabajados)
    else:
        print('spawneado imposible')
        break

