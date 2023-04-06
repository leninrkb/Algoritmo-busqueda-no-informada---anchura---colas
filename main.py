# from numba import njit
import queue
from laberinto import Laberinto
from agente import Agente
import algoritmo
import copy
import time

laberinto = Laberinto()
agente = Agente()
cola = queue.Queue()

# obtengo la forma de la matriz laberinto
# para controlar que el agente no se salga de los limites
agente.maxx, agente.maxy = laberinto.laberinto.shape 

# obtengo las coordenadas que corresponden a la salida
agente.xob, agente.yob = laberinto.fin

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
    print(f'tiempo por una ejecucion completa del agente: {sub_total} segundos')

print(f'tiempo total de la ejecucion: {total} segundos')
print(f'nodos generados: {total_nodos}')



    

