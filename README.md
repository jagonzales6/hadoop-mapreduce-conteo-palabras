# Conteo de palabras con Hadoop MapReduce

Proyecto académico de procesamiento distribuido de texto que realiza el conteo de palabras de un artículo científico en español.

## Tecnologías utilizadas

* Apache Hadoop 3.3.4
* HDFS
* YARN
* Python 3
* mrjob 0.7.4
* OpenJDK 11
* WSL2 con Ubuntu 22.04

## Objetivo

Procesar el texto completo de un artículo científico y generar una salida con la estructura:

`palabra, cantidad`

## Flujo de procesamiento

1. Conversión del artículo PDF a texto con `pdftotext`.
2. Normalización Unicode y conversión a minúsculas.
3. Carga del archivo de entrada en HDFS.
4. Emisión de pares `(palabra, 1)` mediante el mapper.
5. Suma parcial mediante el combiner.
6. Agrupación de palabras durante Shuffle y Sort.
7. Suma final de frecuencias mediante el reducer.
8. Almacenamiento del resultado en HDFS.

## Estructura del proyecto

* `src/conteo_palabras.py`: programa MapReduce.
* `data/README.md`: instrucciones para preparar los datos.
* `results/`: resultados de las ejecuciones.
* `docs/`: informe del proyecto.
* `requirements.txt`: dependencias de Python.

## Instalación

```bash
pip3 install --user -r requirements.txt
```

## Ejecución local

```bash
python3 src/conteo_palabras.py -r local data/articulo.txt
```

## Ejecución con Hadoop

```bash
hdfs dfs -mkdir -p /user/sus/caso_conteo/input
hdfs dfs -put -f data/articulo.txt /user/sus/caso_conteo/input/
hdfs dfs -rm -r -f /user/sus/caso_conteo/output

python3 src/conteo_palabras.py -r hadoop \
  hdfs:///user/sus/caso_conteo/input/articulo.txt \
  --output-dir hdfs:///user/sus/caso_conteo/output
```

## Resultados

El procesamiento produjo 2.381 palabras diferentes.

| Palabra      | Frecuencia |
| ------------ | ---------: |
| artificial   |         22 |
| inteligencia |         16 |
| medicina     |         14 |
| salud        |         12 |
| médico       |          9 |

Los resultados obtenidos localmente coincidieron con los generados mediante Hadoop.
