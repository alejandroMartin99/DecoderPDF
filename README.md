# PDFDecoderAIP

## Resumen
PDFDecoderAIP es un proyecto diseñado para automatizar la comparación entre dos documentos del AIP España, centrándose específicamente en cartas y procedimientos aplicables a LEBL.

El proceso se basa en dos verticales principales:

1. **Scraping de tablas:** Utilizando técnicas de scraping, el programa extrae datos tabulares relevantes de los documentos.
2. **Comparación de imágenes:** Comparando visualmente las imágenes de los documentos para identificar diferencias.

## Instalación
Para utilizar PDFDecoderAIP, asegúrate de tener instaladas las siguientes bibliotecas de Python:
```bash
pip install pandas
pip install camelot-py[cv]
pip install PyPDF2==2.12.1
pip install PyMuPDF


## Uso
1. Clona este repositorio en tu máquina local.
2. Instala las dependencias mencionadas anteriormente.
3. Ejecuta el script principal.

## Contribución
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre una solicitud de extracción.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).
