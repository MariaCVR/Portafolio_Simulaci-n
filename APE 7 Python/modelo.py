import time
import numpy as np

class MonteCarloModel:
    def __init__(self, semilla=42):
        self.semilla = semilla

    def simular_pi(self, n):
        inicio = time.perf_counter()
        
        rng = np.random.default_rng(self.semilla)
        x = rng.random(n)
        y = rng.random(n)
        
        dentro = (x**2 + y**2) <= 1.0
        nc = int(np.sum(dentro))
        
        pi_estimado = 4.0 * (nc / n)
        error_absoluto = abs(np.pi - pi_estimado)
        
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        
        return {
            "N": n,
            "Pi_Estimado": pi_estimado,
            "Error_Absoluto": error_absoluto,
            "Tiempo_Python_ms": tiempo_ms,
            "x": x,
            "y": y,
            "dentro": dentro
        }