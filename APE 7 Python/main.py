from modelo import MonteCarloModel
from vista import MonteCarloView
from controlador import MonteCarloController

if __name__ == "__main__":
    muestras = [1000, 10000, 100000, 1000000]
    
    modelo = MonteCarloModel(semilla=42)
    vista = MonteCarloView()
    controlador = MonteCarloController(modelo, vista)
    
    controlador.ejecutar_experimento(muestras, n_grafico=10000)