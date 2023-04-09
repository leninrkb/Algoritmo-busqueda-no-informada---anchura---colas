from laberinto import Laberinto
from agente import Agente
import queue
import algoritmo #script
import copy
import time
import random
# from memory_profiler import profile

laberinto = Laberinto()
laberinto.laberintoL2()
agente = Agente()
cola = queue.Queue()


# mapeo todas las rutas
camino_laberinto = algoritmo.mapear_camino(laberinto)
# ago que el agente aparesca en una posicion random

#-1 para no exceder el index
posicion_random = random.randint(0, len(camino_laberinto)-1)
agente.posx, agente.posy = camino_laberinto[posicion_random]

print(f'posicion inicial del agente: {agente.posx}, {agente.posy}')

# obtengo la forma de la matriz laberinto
# para controlar que el agente no se salga de los limites
agente.maxx, agente.maxy = laberinto.laberinto.shape 

# obtengo las coordenadas que corresponden a la salida
agente.xob, agente.yob = laberinto.fin

# @profile(stream=open('memory_profile.log', 'w+'))
def inicio(laberinto, cola, agente):
    #agente aqui es semilla!!!!
    #lista para guardar los estados que ya generaron hijos y evitar ciclos
    trabajados = [] 
    total_nodos = 1
    # genero los primeros estados a partir del nodo inicial
    respuesta = algoritmo.generar_estados_posibles(laberinto, agente)
    if isinstance(respuesta, list): 
        total_nodos += len(respuesta)

    # aqui llamo a agregar_cola()
    # cola aqui se pasa como referencia de la original
    algoritmo.control_flujo(respuesta, cola, trabajados) 

    total_tiempo = 0
    while not cola.empty():
        inicio = time.time()

        # obtiene el agente y lo elimina de la cola FIFO!!!
        agente = cola.get() 

        # registro el agente en la lista de trabajados para no volver 
        # a tomarlos en cuenta
        trabajados.append(copy.copy(agente))

        # genero los estados posibles del agente
        respuesta = algoritmo.generar_estados_posibles(laberinto, agente)
        #compruebo q sea una lista para poder contar los nodos
        if isinstance(respuesta, list): 
            total_nodos += len(respuesta)


        # controlo las acciones posteriores, agrego ? termino ? hay solucion ?
        if algoritmo.control_flujo(respuesta, cola, trabajados):
            break
        
        fin = time.time()
        sub_total_tiempo = fin - inicio # tiempo de cada nodo
        total_tiempo += sub_total_tiempo
        print(f'tiempo por una ejecucion completa del agente: {sub_total_tiempo} segundos \n')

    print(f'tiempo total de la ejecucion: {total_tiempo} segundos')
    print(f'nodos generados: {total_nodos}')
inicio(laberinto, cola, agente)



    

