# Proyecto Integrador de Data Science — Fase 1

## Relación entre las condiciones climáticas y el comportamiento de las ventas

Proyecto correspondiente a la Fase 1 — Comprensión, preparación y análisis exploratorio.

### Integrantes

- Diego Torres
- Crista Orué

### Período de estudio

02/01/2021 – 30/09/2021

## Descripción

El proyecto analiza el comportamiento de las ventas minoristas y su posible relación con las condiciones meteorológicas durante el período de estudio.

El análisis utiliza los datos de ventas proporcionados por la cátedra y datos climáticos históricos obtenidos mediante Open-Meteo.

En esta fase se realiza la comprensión de los datos, limpieza y transformación, análisis univariado y bivariado, análisis exploratorio, identificación de patrones y anomalías y formulación de hipótesis preliminares para la Fase 2.

## Estructura del repositorio

```text
proyecto-data-science/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   └── Fase1_DataScience_Grupo6.ipynb
│
├── output/
│   ├── figures/
│   └── tables/
│
├── scripts/
│   └── descargar_datos.py
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Datos

### Datos de ventas

Los datos originales de ventas fueron proporcionados por la cátedra.

El archivo original `ventas.csv` supera el límite de 25 MB establecido para la entrega, por lo que no se incluye dentro del repositorio.

Para obtenerlo, no es necesario realizar una descarga manual. El repositorio incluye el script:

```text
scripts/descargar_datos.py
```

Este script descarga automáticamente el archivo original desde Google Drive y lo guarda en:

```text
data/raw/ventas.csv
```

### Datos climáticos

Los datos meteorológicos históricos fueron obtenidos mediante Open-Meteo.

Se utilizó una ubicación meteorológica de referencia correspondiente a Asunción, Paraguay. La serie climática se relaciona con las ventas mediante la fecha.

La ubicación climática de referencia no se interpreta como la ubicación real de los locales de venta.

## Procesamiento de los datos

Durante la preparación de los datos se realizaron, entre otras, las siguientes tareas:

- Conversión de fechas al formato datetime.
- Conversión de la variable cantidad a formato numérico.
- Limpieza de espacios en variables de texto.
- Validación del período de estudio.
- Identificación de valores faltantes.
- Análisis de registros duplicados.
- Análisis de cantidades negativas.
- Análisis de valores extremos.
- Generación de variables temporales.
- Agregación de las ventas por día y por local.
- Integración de los datos climáticos con las ventas.

Los datasets procesados son generados automáticamente por el notebook y se almacenan en:

```text
data/processed/
```

## Resultados

Los resultados generados durante el análisis incluyen gráficos y tablas.

Los gráficos se generan en:

```text
output/figures/
```

Las tablas se generan en:

```text
output/tables/
```

Estos archivos son productos derivados del análisis y pueden regenerarse ejecutando el notebook.

## Notebook

El notebook principal del proyecto es:

```text
notebooks/Fase1_DataScience_Grupo6.ipynb
```

También se incluye la versión HTML del notebook:

```text
output/Fase1_DataScience_Ventas_Clima.html
```

El notebook contiene el proceso completo de carga, limpieza, transformación, análisis exploratorio e integración de los datos climáticos.

## Requisitos

Se recomienda utilizar Python 3.10 o superior.

Las dependencias utilizadas en el proyecto se encuentran en:

```text
requirements.txt
```

Para instalarlas:

```bash
pip install -r requirements.txt
```

## Reproducción

Para reproducir el análisis desde cero:

### 1. Clonar o descargar el repositorio

Descargar o clonar este repositorio en el equipo local.

### 2. Instalar las dependencias

Desde la carpeta raíz del proyecto ejecutar:

```bash
pip install -r requirements.txt
```

### 3. Descargar los datos originales

Ejecutar el script de descarga:

```bash
python scripts/descargar_datos.py
```

El script descargará automáticamente el dataset original proporcionado por la cátedra y lo colocará en:

```text
data/raw/ventas.csv
```

No es necesario descargar manualmente el archivo desde Google Drive.

### 4. Ejecutar el notebook

Abrir:

```text
notebooks/Fase1_DataScience_Grupo6.ipynb
```

y ejecutar las celdas en orden.

El notebook generará automáticamente los datasets procesados, tablas y gráficos utilizados durante el análisis.

## Fuente de los datos

### Ventas

Dataset proporcionado por la cátedra para el desarrollo del Proyecto Integrador de Data Science.

La descarga se encuentra automatizada mediante:

```text
scripts/descargar_datos.py
```

### Clima

Datos meteorológicos históricos obtenidos mediante Open-Meteo.

La información climática se utiliza como una serie diaria de referencia para Asunción, Paraguay y se integra con los datos de ventas mediante la fecha.

## Fase 1

La Fase 1 comprende:

- Comprensión del problema.
- Comprensión y preparación de los datos.
- Limpieza y transformación.
- Análisis exploratorio.
- Análisis univariado y bivariado.
- Integración de información climática.
- Identificación de patrones y anomalías.
- Formulación de hipótesis preliminares para la Fase 2.