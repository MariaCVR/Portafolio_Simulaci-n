package modelo;

public class ResultadoSimulacion {
    public int n;
    public double piEstimado;
    public double errorAbsoluto;
    public double tiempoMs;
    public double[] xs;
    public double[] ys;
    public boolean[] dentro;

    public ResultadoSimulacion(int n, double piEstimado, double errorAbsoluto, double tiempoMs,
                               double[] xs, double[] ys, boolean[] dentro) {
        this.n = n;
        this.piEstimado = piEstimado;
        this.errorAbsoluto = errorAbsoluto;
        this.tiempoMs = tiempoMs;
        this.xs = xs;
        this.ys = ys;
        this.dentro = dentro;
    }
}