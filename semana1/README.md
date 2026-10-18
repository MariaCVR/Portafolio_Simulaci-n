# Práctica Experimental Nro. 01 - Simulación de Modelo Atmosférico

## 1. Descripción del proyecto
Este proyecto implementa un modelo matemático continuo y discreto para la simulación computacional de condiciones climatológicas horarias (humedad, nubosidad y temperatura).

* **Propósito:** Evaluar e interpretar el comportamiento dinámico del índice de probabilidad de lluvia ($I$) mediante la re-ponderación de parámetros a lo largo de un ciclo diario.
* **Problema resuelto:** Filtrar falsos positivos en diagnósticos de precipitación (ej. temperaturas frías matutinas) mediante la separación de estrategias numéricas y la clasificación por umbrales de riesgo.

## 2. Tecnologías utilizadas
* **Lenguaje de programación:** Python 3.x
* **Librerías principales:** Matplotlib (para la visualización gráfica de tendencias)
* **Patrones de diseño:** Patrón *Strategy* (Programación Orientada a Objetos para desacoplar modelos numéricos)
* **Entorno de desarrollo:** Linux (Ubuntu) / Entorno virtual (`venv`)

## 3. Instalación
Para preparar y configurar el entorno de ejecución, sigue estos pasos:

```bash
# 1. Crear el entorno virtual (si aún no lo has creado)
python3 -m venv venv

# 2. Activar el entorno virtual
source venv/bin/activate

# 3. Instalar dependencias requeridas
pip install matplotlib

#4. Uso
Para ejecutar la simulación, mostrar los resultados en consola y generar las gráficas comparativas:
# Ejecutar el script principal desde la raíz del proyecto
python3 semana1/main.py

#5. Configuración del modelo
El sistema evalúa dos estrategias basadas en la ecuación $I = w_1 \cdot H + w_2 \cdot N + w_3 \cdot T_f$:
Estrategia Base: $w_1 = 0.5$ (Humedad), $w_2 = 0.3$ (Nubosidad), $w_3 = 0.2$ (Temperatura)
Estrategia Ajustada: $w_1 = 0.6$ (Humedad), $w_2 = 0.3$ (Nubosidad), $w_3 = 0.1$ (Temperatura)
#6. Estructura del proyectoPlaintextsemana1/
├── main.py                 # Script principal con el dataset meteorológico de prueba
├── simulacion.py           # Implementación del patrón Strategy y lógica del simulador
├── modelo_base.png         # Gráfica de resultados generada (Modelo Base)
├── modelo_ajustado.png     # Gráfica de resultados generada (Modelo Ajustado)
├── Informe_Practica_01.pdf # Documento técnico formal en formato PDF
└── README.md               # Documentación general de la práctica
#7. Información adicional
Ventana de Precipitaciones: La simulación determina que las horas de mayor probabilidad de lluvia concentrada ($I \ge 0.75$) ocurren entre las 16:00 y las 22:00 horas.Uso de IA: Se utilizó Google Gemini exclusivamente como apoyo técnico para la resolución de errores de terminal y maquetación de informes.Institución: Universidad Nacional de Loja — Carrera de Computación (Asignatura: Simulación).