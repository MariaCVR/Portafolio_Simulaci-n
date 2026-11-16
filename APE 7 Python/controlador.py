class MonteCarloController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_experimento(self, tamanos_muestra, n_grafico=10000):
        resultados = []
        datos_para_graficar = None

        for n in tamanos_muestra:
            resultado = self.modelo.simular_pi(n)
            resultados.append(resultado)
            if n == n_grafico:
                datos_para_graficar = resultado

        self.vista.mostrar_tabla(resultados)
        
        if datos_para_graficar:
            self.vista.mostrar_grafica(datos_para_graficar)