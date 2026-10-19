#  Práctica Nro. 02: Comparación de Modelos de Simulación Poblacional

## 1. Descripción del Proyecto
Este proyecto implementa y compara cuatro paradigmas de modelado y simulación computacional (determinístico, estocástico, discreto y continuo) aplicados al estudio del crecimiento poblacional a partir de un conjunto de datos observados.

* **Propósito:** Diferenciar el comportamiento dinámico y las variaciones que introducen la discretización temporal y la aleatoriedad en los modelos de simulación.
* **Problema Resuelto:** Permite evaluar cuantitativa y gráficamente cómo un modelo matemático aproxima la tendencia real de datos empíricos frente a factores como ruido estocástico o aproximaciones numéricas (Método de Euler).

---

## 2. Tecnologías Utilizadas
* **Lenguaje de Programación:** Python 3.x
* **Librerías Principales:**
  * `NumPy`: Cálculos numéricos y generación de distribución normal aleatoria.
  * `Matplotlib`: Generación y visualización de gráficas comparativas.
* **Entorno de Desarrollo:** Visual Studio Code / Terminal Linux (Ubuntu)
* **Control de Versiones:** Git & GitHub

---

## 3. Instalación
Sigue estos pasos para preparar el entorno e instalar las dependencias:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd semana2
   ```
2. **Crear y activar el entorno virtual**
     ``` bash
      python3 -m venv venv
      source venv/bin/activate
    ```
3. **Instalar las librerias necesarias**
```bash
pip install numpy matplotlib
 ```
## 4. Uso 
Para ejecutar la simulación y visualizar la gráfica comparativa:
* Asegúrate de tener activo el entorno virtual (venv).
* Ejecuta el archivo principal:
    ```bash

    python main.py
    ```

Se desplegará una ventana interactiva mostrando la curva de datos reales junto a los cuatro modelos de simulación.

## 5. **Estructura del proyecto**
semana2/

│

├── modelos.py       # Módulo con la lógica matemática de los 4 modelos

├── main.py          # Script principal que ejecuta los modelos y grafica

├── venv/            # Entorno virtual de Python (ignorado en Git)

└── README.md        # Documentación general del proyecto

* **modelos.py:** Contiene las funciones modelo_deterministico, modelo_discreto, modelo_estocastico y modelo_continuo_euler.
* **main.py:** Define los datos iniciales, calcula la tasa de crecimiento promedio ($r$), ejecuta las funciones del módulo modelos y renderiza la gráfica.

##  6. **Resultados y Preguntas de Control** 
**Respuestas a las Preguntas de Control**
1. **¿Qué representa el arreglo de entrada?**
 Representa la serie temporal de datos reales/empíricos observados a lo largo del tiempo.
2. **Diferencia entre modelo determinístico y estocástico:**
 El determinístico no contiene aleatoriedad (mismas entradas producen siempre la misma salida), mientras que el estocástico incluye variabilidad aleatoria
3. **Efecto de modificar la tasa :**
Un aumento en r acelera el crecimiento exponencial de la población; un valor menor o negativo la ralentiza o reduce.
4. **Parámetro:**
Representa la desviación estándar de la variable aleatoria (nivel de ruido o variabilidad externa).
5. **Aumento del nivel de ruido:**
Produce mayores fluctuaciones e irregularidades en el modelo estocástico.
6. **Diferencia entre modelo discreto y continuo:**
El discreto avanza en intervalos de tiempo fijos (t, t+1), mientras que el continuo evoluciona en un flujo ininterrumpido regulado por ecuaciones diferenciales.
7. **Función del parámetro (dt):**
Es el tamaño del paso de integración en el método numérico de Euler; determina la precisión de la aproximación continua.
8. **Importancia de visualización gráfica:**
Permite contrastar visualmente el comportamiento de cada modelo con los datos reales y detectar desviaciones.
9. **Modelo con comportamiento aleatorio:**
   El modelo estocástico.
   
10. **Cambio al introducir un nuevo arreglo de datos:**
  Se recalculan la población inicial $P_0$ y la tasa $r$, escalando todas las curvas simuladas.





   
   
