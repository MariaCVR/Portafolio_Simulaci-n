from abc import ABC, abstractmethod
from dataclasses import dataclass
import matplotlib.pyplot as plt


# 1. DTO
@dataclass
class WeatherRecord:
    hora: str
    humedad_pct: float
    nubosidad_pct: float
    temp_c: float

    def get_H(self) -> float:
        return self.humedad_pct / 100.0

    def get_N(self) -> float:
        return self.nubosidad_pct / 100.0


# 2. Interfaz Abstracta Estrategia
class ModelStrategy(ABC):
    def calculate_tf(self, temp_c: float) -> float:
        if temp_c <= 10:
            return 1.00
        elif temp_c >= 28:
            return 0.10
        return round(1.0 - (temp_c - 10.0) * 0.05, 2)

    @abstractmethod
    def calculate_index(self, H: float, N: float, Tf: float) -> float:
        pass

    def get_state(self, I: float) -> str:
        if I < 0.40:
            return "Sin lluvia"
        elif I < 0.60:
            return "Baja posibilidad"
        elif I < 0.75:
            return "Lluvia probable"
        else:
            return "Lluvia"


# 3. Estrategias Concretas
class BaseAtmosphericStrategy(ModelStrategy):
    def calculate_index(self, H: float, N: float, Tf: float) -> float:
        return round(0.5 * H + 0.3 * N + 0.2 * Tf, 4)


class AdjustedAtmosphericStrategy(ModelStrategy):
    def calculate_index(self, H: float, N: float, Tf: float) -> float:
        return round(0.6 * H + 0.3 * N + 0.1 * Tf, 4)


# 4. Motor de Simulación (Contexto)
class AtmosphericSimulation:
    def __init__(self, strategy: ModelStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ModelStrategy):
        self.strategy = strategy

    def run(self, records: list[WeatherRecord]) -> list[dict]:
        results = []
        for r in records:
            H = r.get_H()
            N = r.get_N()
            Tf = self.strategy.calculate_tf(r.temp_c)
            I = self.strategy.calculate_index(H, N, Tf)
            estado = self.strategy.get_state(I)

            results.append({
                'hora': r.hora,
                'hum_pct': r.humedad_pct,
                'nub_pct': r.nubosidad_pct,
                'temp': r.temp_c,
                'H': H,
                'N': N,
                'Tf': Tf,
                'I': I,
                'estado': estado
            })
        return results

    def plot_results(self, results: list[dict], title: str):
        horas = [r['hora'] for r in results]
        indices = [r['I'] for r in results]
        humedades = [r['H'] for r in results]
        nubosidades = [r['N'] for r in results]

        plt.figure(figsize=(10, 5))
        plt.plot(horas, indices, marker='o', linewidth=2.5, label='Índice de Lluvia (I)', color='blue')
        plt.plot(horas, humedades, linestyle='--', label='Humedad (H)', color='teal', alpha=0.7)
        plt.plot(horas, nubosidades, linestyle='--', label='Nubosidad (N)', color='gray', alpha=0.7)

        plt.axhline(y=0.75, color='r', linestyle=':', label='Umbral Lluvia (>=0.75)')
        plt.axhline(y=0.60, color='orange', linestyle=':', label='Umbral Probable (>=0.60)')

        plt.title(title, fontsize=12, fontweight='bold')
        plt.xlabel('Hora del Día')
        plt.ylabel('Valor Normalizado / Índice')
        plt.ylim(0, 1.05)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend(loc='upper left')
        plt.tight_layout()

        # Guardar en imagen para no bloquear la consola
        nombre_archivo = f"{title.lower().replace(' ', '_')}.png"
        plt.savefig(nombre_archivo)
        plt.close()
        print(f"-> Gráfica guardada como: {nombre_archivo}")


# 5. Función Auxiliar para la Tabla
def print_table(results: list[dict], title: str):
    print(f"\n=== {title} ===")
    print(f"{'Hora':<7} | {'H':<5} | {'N':<5} | {'Tf':<5} | {'Índice (I)':<10} | {'Estado'}")
    print("-" * 55)
    for r in results:
        print(f"{r['hora']:<7} | {r['H']:<5.2f} | {r['N']:<5.2f} | {r['Tf']:<5.2f} | {r['I']:<10.4f} | {r['estado']}")