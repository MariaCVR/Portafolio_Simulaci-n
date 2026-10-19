import numpy as np
import matplotlib.pyplot as plt
from modelos import (
    modelo_deterministico,
    modelo_discreto,
    modelo_estocastico,
    modelo_continuo_euler
)

def ejecutar_simulacion():
    # Datos de entrada asignados
    datos = [1000, 1100, 1250, 1400, 1600, 1850, 2100]

    # Parámetros base
    P0 = datos[0]                     # Población inicial (1000)
    tiempo = len(datos) - 1           # Número de períodos (6)
    
    # Estimación de la tasa promedio de crecimiento (r)
    tasas = [(datos[i+1] - datos[i]) / datos[i] for i in range(len(datos) - 1)]
    r = np.mean(tasas)

    sigma = 30                        # Nivel de aleatoriedad / ruido
    dt = 0.1                          # Tamaño del paso para Euler

    # Ejecución de los modelos
    t_det, p_det = modelo_deterministico(P0, r, tiempo)
    t_disc, p_disc = modelo_discreto(P0, r, tiempo)
    t_estoc, p_estoc = modelo_estocastico(P0, r, sigma, tiempo)
    t_cont, p_cont = modelo_continuo_euler(P0, r, tiempo, dt)

    # Gráfica Comparativa
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(datos)), datos, 'ko--', label='Datos reales de entrada', linewidth=2)
    plt.plot(t_det, p_det, 'b-', label='Modelo Determinístico', linewidth=2)
    plt.plot(t_disc, p_disc, 'g--o', label='Modelo Discreto')
    plt.plot(t_estoc, p_estoc, 'r-s', label='Modelo Estocástico')
    plt.plot(t_cont, p_cont, 'm:', label='Modelo Continuo (Euler)', linewidth=2)

    plt.title('Comparación de Modelos de Simulación Poblacional')
    plt.xlabel('Tiempo')
    plt.ylabel('Población')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    ejecutar_simulacion()