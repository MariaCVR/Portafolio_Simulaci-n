package vista;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.Stroke;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.List;
import javax.imageio.ImageIO;
import modelo.ResultadoSimulacion;

public class MonteCarloView {
    public void mostrarTabla(List<ResultadoSimulacion> resultados) {
        System.out.println("\n=== RESULTADOS EN JAVA ===");
        System.out.printf("%-10s | %-12s | %-15s | %-16s%n", "N", "Pi Estimado", "Error Absoluto", "Tiempo Java (ms)");
        System.out.println("-------------------------------------------------------------");

        for (ResultadoSimulacion r : resultados) {
            System.out.printf("%-10d | %-12.6f | %-15.6f | %-16.4f%n",
                r.n, r.piEstimado, r.errorAbsoluto, r.tiempoMs);
        }
    }

    public void guardarGrafica(ResultadoSimulacion datos) {
        int tam = 750;
        int margenIzq = 80;
        int margenDer = 50;
        int margenSup = 70;
        int area = tam - margenIzq - margenDer;

        BufferedImage img = new BufferedImage(tam, tam, BufferedImage.TYPE_INT_RGB);
        Graphics2D g = img.createGraphics();
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Fondo blanco
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, tam, tam);

        // Cuadrícula punteada y números de los ejes (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
        g.setFont(new Font("SansSerif", Font.PLAIN, 13));
        Stroke lineaNormal = g.getStroke();
        Stroke lineaPunteada = new BasicStroke(1, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0, new float[]{4}, 0);

        for (int i = 0; i <= 5; i++) {
            double valor = i * 0.2;
            String texto = String.format("%.1f", valor);
            int offset = (int) (valor * area);

            // Eje X (abajo)
            int xPos = margenIzq + offset;
            g.setColor(new Color(220, 220, 220));
            g.setStroke(lineaPunteada);
            g.drawLine(xPos, margenSup, xPos, margenSup + area);

            g.setColor(Color.BLACK);
            g.setStroke(lineaNormal);
            g.drawLine(xPos, margenSup + area, xPos, margenSup + area + 5);
            g.drawString(texto, xPos - 10, margenSup + area + 23);

            // Eje Y (izquierda)
            int yPos = (margenSup + area) - offset;
            g.setColor(new Color(220, 220, 220));
            g.setStroke(lineaPunteada);
            g.drawLine(margenIzq, yPos, margenIzq + area, yPos);

            g.setColor(Color.BLACK);
            g.setStroke(lineaNormal);
            g.drawLine(margenIzq - 5, yPos, margenIzq, yPos);
            g.drawString(texto, margenIzq - 35, yPos + 5);
        }

        // Dibujar puntos (azul dentro, naranja fuera)
        Color azul = new Color(31, 119, 180);
        Color naranja = new Color(255, 127, 14);

        for (int i = 0; i < datos.n; i++) {
            int px = margenIzq + (int) (datos.xs[i] * area);
            int py = (margenSup + area) - (int) (datos.ys[i] * area);
            g.setColor(datos.dentro[i] ? azul : naranja);
            g.fillOval(px - 2, py - 2, 4, 4);
        }

        // Marco exterior del gráfico
        g.setColor(Color.BLACK);
        g.drawRect(margenIzq, margenSup, area, area);

        // Título y nombres de ejes
        g.setFont(new Font("SansSerif", Font.BOLD, 17));
        g.drawString("Simulación Monte Carlo para π (N = " + String.format("%,d", datos.n) + ")", margenIzq + 110, 40);

        g.setFont(new Font("SansSerif", Font.BOLD, 14));
        g.drawString("x", margenIzq + (area / 2), margenSup + area + 50);
        g.drawString("y", 25, margenSup + (area / 2));

        // Leyenda en la esquina superior derecha
        int legX = margenIzq + area - 195;
        int legY = margenSup + 15;
        g.setColor(new Color(255, 255, 255, 235));
        g.fillRect(legX, legY, 180, 52);
        g.setColor(Color.GRAY);
        g.drawRect(legX, legY, 180, 52);

        g.setFont(new Font("SansSerif", Font.PLAIN, 12));
        g.setColor(azul);
        g.fillOval(legX + 10, legY + 13, 8, 8);
        g.setColor(Color.BLACK);
        g.drawString("Dentro (x² + y² ≤ 1)", legX + 25, legY + 21);

        g.setColor(naranja);
        g.fillOval(legX + 10, legY + 33, 8, 8);
        g.setColor(Color.BLACK);
        g.drawString("Fuera", legX + 25, legY + 41);

        g.dispose();

        try {
            File salida = new File("grafica_montecarlo_java.png");
            ImageIO.write(img, "png", salida);
            System.out.println("\n[OK] Imagen guardada en: " + salida.getAbsolutePath());
        } catch (Exception e) {
            System.out.println("Error al guardar la imagen: " + e.getMessage());
        }
    }
}