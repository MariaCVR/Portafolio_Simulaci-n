from simulacion import (
    WeatherRecord,
    BaseAtmosphericStrategy,
    AdjustedAtmosphericStrategy,
    AtmosphericSimulation,
    print_table,
)

def main():
    records = [
        WeatherRecord("06:00", humedad_pct=65.0, nubosidad_pct=40.0, temp_c=14.0),
        WeatherRecord("08:00", humedad_pct=70.0, nubosidad_pct=50.0, temp_c=16.0),
        WeatherRecord("10:00", humedad_pct=68.0, nubosidad_pct=45.0, temp_c=18.0),
        WeatherRecord("12:00", humedad_pct=60.0, nubosidad_pct=30.0, temp_c=22.0),
        WeatherRecord("14:00", humedad_pct=75.0, nubosidad_pct=70.0, temp_c=20.0),
        WeatherRecord("16:00", humedad_pct=85.0, nubosidad_pct=85.0, temp_c=18.0),
        WeatherRecord("18:00", humedad_pct=92.0, nubosidad_pct=95.0, temp_c=16.0),
        WeatherRecord("20:00", humedad_pct=88.0, nubosidad_pct=90.0, temp_c=15.0),
        WeatherRecord("22:00", humedad_pct=80.0, nubosidad_pct=75.0, temp_c=15.0),
    ]

    # 1. MODELO BASE
    sim = AtmosphericSimulation(strategy=BaseAtmosphericStrategy())
    results_base = sim.run(records)
    print_table(results_base, "RESULTADOS MODELO BASE")
    sim.plot_results(results_base, "Modelo Base")

    # 2. MODELO AJUSTADO
    sim.set_strategy(AdjustedAtmosphericStrategy())
    results_adj = sim.run(records)
    print_table(results_adj, "RESULTADOS MODELO AJUSTADO")
    sim.plot_results(results_adj, "Modelo Ajustado")


if __name__ == "__main__":
    main()