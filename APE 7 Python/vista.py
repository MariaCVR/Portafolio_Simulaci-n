import matplotlib.pyplot as plt

class MonteCarloView:
    def mostrar_tabla(self, resultados):
        print("\n=== RESULTADOS EN PYTHON ===")
        print(f"{'N':<10} | {'Pi Estimado':<12} | {'Error Absoluto':<15} | {'Tiempo Python (ms)':<18}")
        print("-" * 64)
        for r in resultados:
            print(f"{r['N']:<10} | {r['Pi_Estimado']:<12.6f} | {r['Error_Absoluto']:<15.6f} | {r['Tiempo_Python_ms']:<18.4f}")

    def mostrar_grafica(self, datos_muestra):
        x = datos_muestra["x"]
        y = datos_muestra["y"]
        dentro = datos_muestra["dentro"]
        n = datos_muestra["N"]

        plt.figure(figsize=(6, 6))
        plt.scatter(x[dentro], y[dentro], color='#1f77b4', s=2, label=r'Dentro ($x^2+y^2 \leq 1$)')
        plt.scatter(x[~dentro], y[~dentro], color='#ff7f0e', s=2, label='Fuera')
        plt.title(rf'Simulación Monte Carlo para $\pi$ (N = {n:,})')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc='upper right')
        plt.axis('equal')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.savefig('grafica_montecarlo.png', dpi=300)
        plt.show()