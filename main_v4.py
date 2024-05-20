import os
import camelot
import pandas as pd
import fitz 

from Modules.extract_tables_with_string   import extract_tables_with_string
from Modules.compare_and_save_tables      import compare_and_save_tables
from Modules.generate_difference_image    import generate_difference_image
from Modules.save_format_frontend         import save_format_frontend

os.system('cls')

# Carpeta donde se encuentran los PDFs
pdf_folder = 'Compare_2_PDFs'
pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

tables_coordinates = []
tables_description = []

print(f'Se inicia la comparación de tablas:')

for pdf_file in pdf_files:
    print(f'Extrayendo tablas de {pdf_file} ...')
    
    tables_coord = extract_tables_with_string(
        pdf_file, 
        "COORDENADAS WAYPOINTS // WAYPOINTS COORDINATES", 
        index_offset=1, 
        header_change=True
    )
    tables_coordinates.append(tables_coord)
    print(f'...tabla COORDENADAS correctamente encontrada y procesada. \u2713')

    tables_desc = extract_tables_with_string(
        pdf_file, 
        "DESCRIPCIÓN TABULAR DEL PROCEDIMIENTO", 
        index_offset=11,
        column_names=[
            'Serial number', 
            'Path Terminator', 
            'Waypoint identifier',
            'Fly-over', 
            'Course/Track', 
            'Magnetic variation', 
            'Distance',
            'Turn direction', 
            'Altitude', 
            'Speed', 
            'VPA/TCH',
            'Navegation specification'
            ]
        )

    tables_description.append(tables_desc)

    print(f'...tabla DESCRIPCIÓN TABULAR correctamente encontrada y procesada. \u2713')
    print(' ')


df_tables_coord = compare_and_save_tables(tables_coordinates)
df_tables_desc = compare_and_save_tables(tables_description)


output_path = ( 'Result_Output_V1.0.xlsx')
save_format_frontend(
    output_path,
    [
        df_tables_coord,
        df_tables_desc,
    ],
    [
        'Coordenadas',
        'DescripcionTabular',
        ]
)
print(f'Se ha generado correctamente el fichero excel donde se recogen los cambios. \u2713')

print(f'\nSe inicia la comparación de imágenes:\nLista de PDF:')
for i in range(len(pdf_files)-1):
    pdf1_path = pdf_files[i]
    print(f'PDF1: {pdf1_path}')
    pdf2_path = pdf_files[i+1]
    print(f'PDF2: {pdf2_path}')

pages_to_compare = [0,1,2,3]
print(f'Se van a comparar las páginas siguientes: {pages_to_compare}')

for page in pages_to_compare:
    output_image_path = f'differences_page_{page}.jpg'
    generate_difference_image(pdf1_path, pdf2_path, [page], output_image_path)
