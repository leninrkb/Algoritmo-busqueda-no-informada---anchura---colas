# Algoritmo de busqueda no informado

## Problema
Un dispositivo se encuentra en un laberinto y debe buscar la salida. este dispositivo ha de comprobar posibles movimientos y detectar muros, de esta forma podra encontrar la salida.

## Solucion
Un algoritmo de inteligencia artificial no informado con busqueda por anchura utilizando colas, que genere un agente capas de realizar todos los movimientos posibles para hallar la salida. Cada mov del agente genera un nuevo nodo en el arbol.
Se ha de comprobar si el nodo actual o el proximo es una solucion para detener el algoritmo.

## Algoritmo de busqueda no informado
- importa el camino
- la funcion objetivo indica el camino
### Primero profundidad
- mas costo matematico
### Por anchura
- mas memoria
### Profundidad iterativa
- trata de optimizar el uso de memoria y el costo matematico
### Bidireccionales
- menor costo computacional


## Recursos
Puedes crear un entorno nuevo de conda: ```conda create -n algoritmos_ia python=3.8 ```
- numba: ```pip install numba```

njit es un decorador de la librería numba de Python que se utiliza para mejorar la velocidad de ejecución de funciones de Python. numba es una librería de compilación Just-In-Time (JIT) que optimiza y acelera el código de Python a través de la compilación en tiempo de ejecución.

- memory_profiler: ```pip install memory_profiler```

Este módulo proporciona una forma sencilla de medir el uso de memoria de una función en particular.