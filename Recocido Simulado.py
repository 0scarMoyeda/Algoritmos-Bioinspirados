import math
import random

def funcion_objetivo(x):
    # Función cuadrática de ejemplo
    return x**2

def recocido_simulado(funcion_objetivo, temperatura_inicial, temperatura_final, enfriamiento, iteraciones):
    solucion_actual = random.uniform(-10, 10)  # Punto de inicio aleatorio
    costo_actual = funcion_objetivo(solucion_actual)

    mejor_solucion = solucion_actual
    mejor_costo = costo_actual

    temperatura_actual = temperatura_inicial

    for _ in range(iteraciones):
        vecino = solucion_actual + random.uniform(-0.5, 0.5)  # Generar un vecino aleatorio

        costo_vecino = funcion_objetivo(vecino)

        # Probabilidad de aceptar el vecino como la nueva solución
        probabilidad_aceptacion = math.exp((costo_actual - costo_vecino) / temperatura_actual)

        if costo_vecino < costo_actual or random.uniform(0, 1) < probabilidad_aceptacion:
            solucion_actual = vecino
            costo_actual = costo_vecino

        # Actualizar la mejor solución encontrada hasta ahora
        if costo_actual < mejor_costo:
            mejor_solucion = solucion_actual
            mejor_costo = costo_actual

        # Enfriar la temperatura
        temperatura_actual *= enfriamiento

        # Asegurarse de que la temperatura no sea menor que la temperatura final
        temperatura_actual = max(temperatura_actual, temperatura_final)

    return mejor_solucion, mejor_costo

# Parámetros del algoritmo
temperatura_inicial = 1000
temperatura_final = 1
enfriamiento = 0.95
iteraciones = 1000

# Ejecutar el recocido simulado
solucion, costo = recocido_simulado(funcion_objetivo, temperatura_inicial, temperatura_final, enfriamiento, iteraciones)

print(f"Mejor solución encontrada: {solucion}")
print(f"Valor de la función objetivo en la mejor solución: {costo}")