import copy
import numpy as np
import queue

def generar_estados_posibles(laberinto, agente):
    '''este metodo genera los cuatro estados basicos posibles,
    y retorna una lista con los que se lograron generar. 
    cada agente guarda su gente padre'''

    lista = []
    if agente.es_funcion_objetivo():
        imprimir_ruta(agente)
        return True
    if laberinto.laberinto[agente.posx][agente.posy] == 1:
        agente_arriba = copy.copy(agente)
        agente_abajo = copy.copy(agente)
        agente_izquierda = copy.copy(agente)
        agente_derecha = copy.copy(agente)

        if agente_arriba.arriba():
            if laberinto.laberinto[agente_arriba.posx][agente_arriba.posy] == 1:
                print(agente_arriba.posx, agente_arriba.posy)
                agente_arriba.padre = agente
                lista.append(agente_arriba)
            else:
                print('se encontro con una pared arriba')
        else:
            print('no puede ir mas arriba')
        if agente_abajo.abajo():
            if laberinto.laberinto[agente_abajo.posx][agente_abajo.posy] == 1:
                print(agente_abajo.posx, agente_abajo.posy)
                agente_abajo.padre = agente
                lista.append(agente_abajo)

            else:
                print('se encontro con una pared abajo')
        else:
            print('no puede ir mas abajo')
        if agente_izquierda.izquierda():
            if laberinto.laberinto[agente_izquierda.posx][agente_izquierda.posy] == 1:
                print(agente_izquierda.posx, agente_izquierda.posy)
                agente_izquierda.padre = agente
                lista.append(agente_izquierda)

            else:
                print('se encontro con una pared a la izquierda')
        else:
            print('no puede ir mas izquierda')
        if agente_derecha.derecha():
            if laberinto.laberinto[agente_derecha.posx][agente_derecha.posy] == 1:
                print(agente_derecha.posx, agente_derecha.posy)
                agente_derecha.padre = agente
                lista.append(agente_derecha)

            else:
                print('se encontro con una pared a la derecha')
        else:
            print('no puede ir mas derecha')
        print('\n')
        return lista
    else:
        print('el agente spawneo en un lugar imposible')
        return None


def agregar_agentes_cola(cola, lista_agentes, trabajados):
    for agente in lista_agentes:
        if es_repetido(agente, trabajados):
            continue
        cola.put(agente)

def es_repetido(agente, trabajados):
    for aux_agente in trabajados:
        if aux_agente.posx == agente.posx and aux_agente.posy == agente.posy:
            return True
    return False


def imprimir_ruta(agente):
    if agente == None:
        return
    print(f'posicion x: {agente.posx} - posicion y: {agente.posy}')
    imprimir_ruta(agente.padre)
