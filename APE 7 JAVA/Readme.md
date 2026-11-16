# Simulación del Método de Monte Carlo para la Estimación de π (Python y Java)

## 1. Descripción del proyecto
Este proyecto implementa una simulación estocástica basada en el **Método de Monte Carlo** para estimar el valor de la constante matemática $\pi$ mediante la generación de puntos aleatorios uniformemente distribuidos en el primer cuadrante del plano cartesiano ($[0,1] \times [0,1]$). 

**Propósito y problema resuelto:**
* Evaluar la convergencia estadística y precisión del estimador ($\hat{\pi} = 4 \cdot \frac{n_c}{N}$) frente al valor teórico de $\pi$ al incrementar el tamaño de muestra ($N \in \{1\,000, 10\,000, 100\,000, 1\,000\,000\}$).
* Comparar el rendimiento computacional (tiempos de ejecución en milisegundos) entre un entorno interpretado con vectorización numérica (**Python**) y un entorno compilado tipado (**Java**).
* Implementar ambos desarrollos bajo la arquitectura **Modelo-Vista-Controlador (MVC)** con salida tabular en consola y generación de evidencia gráfica de dispersión para $N = 10\,000$.

---

## 2. Tecnologías utilizadas

### Implementación en Python
* **Lenguaje:** Python 3.x
* **Librerías:** `NumPy` (cálculo numérico y generación vectorizada de números pseudoaleatorios con semilla fija), `Matplotlib` (gráficas de dispersión y exportación de imágenes) y `time` (medición de tiempos de ejecución).

### Implementación en Java
* **Lenguaje:** Java (JDK 17+)
* **Librerías nativas (sin dependencias externas):** `java.util.Random` (generación estocástica reproducible), `java.awt.Graphics2D` y `javax.imageio.ImageIO` (renderizado nativo de ejes, cuadrícula, leyenda y exportación en formato `.png`).

---

## 3. Instalación y configuración
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/MariaCVR/Portafolio_Simulaci-n.git](https://github``.com/MariaCVR/Portafolio_Simulaci-n.git)
   cd Portafolio_Simulaci-n
   ```

2. **Preparar el entorno de Python:**
   * **Windows:**
```powershell
pip install numpy matplotlib
```
   * **Linux (Ubuntu/Debian):**
```bash
sudo apt update && sudo apt install -y python3-numpy python3-matplotlib
```

3. **Preparar el entorno de Java:**
   * Verifica tener instalado el **JDK** en tus variables de entorno (`java -version` y `javac -version`). No requiere librerías externas.

---

## 4. Uso

### Ejecutar versión en Python
```bash
cd "APE 7 Python"
python main.py    # En Linux: python3 main.py
```
> **Salida esperada:** Tabla comparativa en consola ($N$, $\hat{\pi}$, error absoluto y tiempo en ms) y generación del archivo `grafica_montecarlo.png`.

### Ejecutar versión en Java
```bash
cd "APE 7 JAVA"
javac Main.java modelo/*.java vista/*.java controlador/*.java
java Main
```
> **Salida esperada:** Tabla comparativa en consola y generación automática de `grafica_montecarlo_java.png` con los puntos interiores ($x^2 + y^2 \le 1$) y exteriores.

---

## 5. Estructura del proyecto

```text
Portafolio_Simulaci-n/
├── APE 7 Python/
│   ├── modelo.py                   # Lógica matemática de Monte Carlo y cálculo de errores
│   ├── vista.py                    # Tablas en consola y gráfico de dispersión con Matplotlib
│   ├── controlador.py              # Orquestación de muestras y flujo entre modelo y vista
│   ├── main.py                     # Punto de entrada de la simulación en Python
│   └── grafica_montecarlo.png      # Evidencia visual generada (N = 10,000)
│
├── APE 7 JAVA/
│   ├── modelo/
│   │   ├── MonteCarloModel.java      # Simulación estocástica con semilla fija (42L)
│   │   └── ResultadoSimulacion.java  # Estructura de datos para métricas y coordenadas
│   ├── vista/
│   │   └── MonteCarloView.java       # Salida en consola y renderizado gráfico con Graphics2D
│   ├── controlador/
│   │   └── MonteCarloController.java # Coordinación de experimentos y muestra gráfica
│   ├── Main.java                     # Punto de entrada de la aplicación en Java
│   └── grafica_montecarlo_java.png   # Evidencia visual generada (N = 10,000)
│
└── README.md                         # Documentación general del repositorio
```
