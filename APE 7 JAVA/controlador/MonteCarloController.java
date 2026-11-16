package controlador;

import java.util.ArrayList;
import java.util.List;
import modelo.MonteCarloModel;
import modelo.ResultadoSimulacion;
import vista.MonteCarloView;

public class MonteCarloController {
    private final MonteCarloModel modelo;
    private final MonteCarloView vista;

    public MonteCarloController(MonteCarloModel modelo, MonteCarloView vista) {
        this.modelo = modelo;
        this.vista = vista;
    }

    public void ejecutarExperimento(int[] tamanosMuestra, int nGrafico) {
        List<ResultadoSimulacion> resultados = new ArrayList<>();
        ResultadoSimulacion paraGraficar = null;

        for (int n : tamanosMuestra) {
            boolean esGrafico = (n == nGrafico);
            ResultadoSimulacion res = modelo.simularPi(n, esGrafico);
            resultados.add(res);
            if (esGrafico) {
                paraGraficar = res;
            }
        }

        vista.mostrarTabla(resultados);
        if (paraGraficar != null) {
            vista.guardarGrafica(paraGraficar);
        }
    }
}