# from numba import njit
from laberinto import Laberinto
from agente import Agente
import queue
import algoritmo
import copy
import time
import random
# from memory_profiler import profile

laberinto = Laberinto()
laberinto.laberintoL1()
agente = Agente()
cola = queue.Queue()

# mapeo todas las rutas
mapa_laberinto = algoritmo.mapear_camino(laberinto)
# ago que el agente aparesca en una posicion random
agente.posx, agente.posy = mapa_laberinto[random.randint(0, len(mapa_laberinto))]

print(f'posicion inicial del agente: {agente.posx}, {agente.posy}')

# obtengo la forma de la matriz laberinto
# para controlar que el agente no se salga de los limites
agente.maxx, agente.maxy = laberinto.laberinto.shape 

# obtengo las coordenadas que corresponden a la salida
agente.xob, agente.yob = laberinto.fin

# @profile(stream=open('memory_profile.log', 'w+'))
def inicio(laberinto, cola, agente):
    #lista para guardar los estados que ya generaron hijos y evitar ciclos
    trabajados = [] 

    total_nodos = 1

    # genero los primeros estados a partir del nodo inicial
    resp = algoritmo.generar_estados_posibles(laberinto, agente)
    if isinstance(resp, list): 
        total_nodos += len(resp)

    algoritmo.control_flujo(resp, cola, trabajados)

    total = 0
    while not cola.empty():
        inicio = time.time()

        # obtiene el agente y lo elimina de la cola
        agente = cola.get() 

        # registro el agente en la lista de trabajados para no volver 
        # a tomarlos en cuenta
        trabajados.append(copy.copy(agente))

        # genero los estados posibles del agente
        resp = algoritmo.generar_estados_posibles(laberinto, agente)
        if isinstance(resp, list): 
            total_nodos += len(resp)


        # controlo las acciones posteriores
        if algoritmo.control_flujo(resp, cola, trabajados):
            break
        
        fin = time.time()
        sub_total = fin - inicio
        total += sub_total
        print(f'tiempo por una ejecucion completa del agente: {sub_total} segundos \n')

    print(f'tiempo total de la ejecucion: {total} segundos')
    print(f'nodos generados: {total_nodos}')
inicio(laberinto, cola, agente)



    

