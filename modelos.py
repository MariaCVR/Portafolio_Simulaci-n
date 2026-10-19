import numpy as np

def modelo_deterministico(P0, r, tiempo):
    """
    Modelo determinístico: P(t) = P0 * e^(r*t)
    """
    t_vector = np.arange(0, tiempo + 1)
    poblacion = P0 * np.exp(r * t_vector)
    return t_vector, poblacion

def modelo_discreto(P0, r, tiempo):
    """
    Modelo discreto: P_{t+1} = P_t + r * P_t
    """
    poblacion = [P0]
    for _ in range(tiempo):
        p_actual = poblacion[-1]
        incremento = r * p_actual
        poblacion.append(p_actual + incremento)
    return list(range(tiempo + 1)), poblacion

def modelo_estocastico(P0, r, sigma, tiempo, semilla=42):
    """
    Modelo estocástico: P_{t+1} = P_t + r * P_t + ruido
    """
    if semilla is not None:
        np.random.seed(semilla)
        
    poblacion = [P0]
    for _ in range(tiempo):
        ruido = np.random.normal(0, sigma)
        p_actual = poblacion[-1]
        nueva_pob = p_actual + (r * p_actual) + ruido
        if nueva_pob < 0:
            nueva_pob = 0.0
        poblacion.append(nueva_pob)
    return list(range(tiempo + 1)), poblacion

def modelo_continuo_euler(P0, r, tiempo, dt):
    """
    Modelo continuo mediante Euler: P_{t+dt} = P_t + dt * (r * P_t)
    """
    t_vector = np.arange(0, tiempo + dt, dt)
    poblacion = [P0]
    for _ in t_vector[:-1]:
        p_actual = poblacion[-1]
        cambio = r * p_actual
        poblacion.append(p_actual + dt * cambio)
    return t_vector, poblacion