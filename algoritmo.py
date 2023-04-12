import copy
import numpy as np
import logging #para usar y crear un archivo log

np.set_printoptions(linewidth=200)
#configuracion basica para usar loggin
logging.basicConfig(filename='resultado.log', level=logging.INFO, filemode='w', format='%(levelname)s:%(name)s:\n%(message)s')



def generar_estados_posibles(laberinto, agente, verbose=False):
    '''este metodo genera los cuatro estados basicos posibles,
    y retorna una lista con los que se lograron generar. 
    cada agente guarda su gente padre'''

    # compruebo si el agente ya corresponde a mi
    # funcion objetivo
    if agente.es_funcion_objetivo():
        ruta = recuperar_ruta(agente,[])
        imprimir_ruta(ruta, laberinto)
        logging.info('esta es la ruta:')
        logging.info(ruta)
        return True
    
    # lista a retornar con los nuevos agentes
    estados_posibles = []
    
    # compruebo si el a gente aparecio en un lugar posible en el
    # laberinto
    if laberinto.laberinto[agente.posx][agente.posy] == 1:
        # genera una copia del padre para generar los agenets hijos
        agente_arriba = copy.copy(agente)
        agente_abajo = copy.copy(agente)
        agente_izquierda = copy.copy(agente)
        agente_derecha = copy.copy(agente)

        # compruebo si el movimiento a realizar esta dentro del laberinto
        if agente_arriba.arriba():
            # comrpuebo si el movimiento es posible dentro del camino
            # y no es un muro
            if laberinto.laberinto[agente_arriba.posx][agente_arriba.posy] == 1:
                if verbose: print(agente_arriba.posx, agente_arriba.posy)
                # es camino y no se sale de los limites, entonces agrego
                agente_arriba.padre = agente
                estados_posibles.append(agente_arriba)
            else:
                if verbose: print('se encontro con una pared arriba')
        else:
            if verbose: print('no puede ir mas arriba')
        if agente_abajo.abajo():
            if laberinto.laberinto[agente_abajo.posx][agente_abajo.posy] == 1:
                if verbose: print(agente_abajo.posx, agente_abajo.posy)
                agente_abajo.padre = agente
                estados_posibles.append(agente_abajo)

            else:
                if verbose: print('se encontro con una pared abajo')
        else:
            if verbose: print('no puede ir mas abajo')
        if agente_izquierda.izquierda():
            if laberinto.laberinto[agente_izquierda.posx][agente_izquierda.posy] == 1:
                if verbose: print(agente_izquierda.posx, agente_izquierda.posy)
                agente_izquierda.padre = agente
                estados_posibles.append(agente_izquierda)

            else:
                if verbose: print('se encontro con una pared a la izquierda')
        else:
            if verbose: print('no puede ir mas izquierda')
        if agente_derecha.derecha():
            if laberinto.laberinto[agente_derecha.posx][agente_derecha.posy] == 1:
                if verbose: print(agente_derecha.posx, agente_derecha.posy)
                agente_derecha.padre = agente
                estados_posibles.append(agente_derecha)

            else:
                if verbose: print('se encontro con una pared a la derecha')
        else:
            if verbose: print('no puede ir mas derecha')
        return estados_posibles
    else:
        return None


def agregar_agentes_cola(cola, lista_agentes, trabajados):
    ''' agrega una lista de agentes a la cola '''
    #tengo que verificar si es repetido o no para poder agregar a la cola
    for agente in lista_agentes:
        if es_repetido(agente, trabajados):
            continue
        cola.put(agente)

def es_repetido(agente, trabajados):
    ''' verifica si la posicion del agente 
     ya existio '''
    for aux_agente in trabajados:
        if aux_agente.posx == agente.posx and aux_agente.posy == agente.posy:
            return True
    return False


def recuperar_ruta(agente, ruta):
    ''' imprime la ruta del agente que llego al objetivo '''
    if agente == None:
        return ruta
    ruta.append((agente.posx,agente.posy))
    return recuperar_ruta(agente.padre, ruta)

def imprimir_ruta(ruta, laberinto):
   

    xlen , ylen = laberinto.laberinto.shape
    #creo una matriz de las miams dimensiones que lab
    laberinto_resuelto = np.empty((xlen,ylen), dtype=object) 
    # relleno esa matriz con ''
    laberinto_resuelto[:] = ' '
    # pongo 1 en el camino hacia la salida conforme a la ruta recuperada
    for posx, posy in ruta:
        laberinto_resuelto[posx, posy] = '1'

    #imprimo en el archivo resultado.log
    logging.info(laberinto_resuelto)

def control_flujo(resp, cola, trabajados):
    if resp == True:
        print('--- solucion encontrada ---')
        return True
    elif not resp == None:
        agregar_agentes_cola(cola, resp, trabajados)
        return False
    else:
        print('spawneado imposible')
        return False
    
def mapear_camino(laberinto):
    xlen, ylen = laberinto.laberinto.shape
    camino_laberinto = []
    for i in range(xlen):
        for j in range(ylen):
            lab = laberinto.laberinto[i][j]
            if lab == 1:
                camino_laberinto.append((i,j)) #agrego la tupla con las coordenadas
    return camino_laberinto
