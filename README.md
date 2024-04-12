# PDFDecoderAIP

## Resumen
PDFDecoderAIP es un proyecto diseñado para automatizar la comparación entre dos documentos del AIP España, centrándose específicamente en cartas y procedimientos aplicables a LEBL. (https://aip.enaire.es/AIP/#LEBL)

El proceso se basa en dos verticales principales:

1. **Scraping de tablas:** Utilizando técnicas de scraping, el programa extrae datos tabulares relevantes de los documentos.
[Texto alternativo](url_de_la_imagen)

2. **Comparación de imágenes:** Comparando visualmente las imágenes de los documentos para identificar diferencias. ![Texto alternativo](url_de_la_imagen)

## Instalación
Para utilizar PDFDecoderAIP, asegúrate de tener instaladas las siguientes bibliotecas de Python:
```bash
pip install pandas
pip install camelot-py[cv]
pip install PyPDF2==2.12.1
pip install PyMuPDF
```

## Uso
1. Clona este repositorio en tu máquina local.
2. Instala las dependencias mencionadas anteriormente.
3. Se deben almacenar los dos PDFs a comparar en la carpeta Compare_2_PDFs.
4. Ejecuta el script principal.

## Estructura del Proyecto


## Licencia

