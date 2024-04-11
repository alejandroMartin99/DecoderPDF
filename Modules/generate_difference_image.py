import numpy as np
from PIL import Image
import fitz

def generate_difference_image(pdf1_path, pdf2_path, different_pages, output_image_path, output_dpi=300, output_quality=100):
    # Abre los documentos PDF
    pdf1_doc = fitz.open(pdf1_path)
    pdf2_doc = fitz.open(pdf2_path)

    # Resaltado en rojo para las diferencias
    red_highlight = (255, 0, 0)  # Rojo

    for page_number in different_pages:
        # Carga las páginas correspondientes de cada PDF
        pdf1_page = pdf1_doc.load_page(page_number)
        pdf2_page = pdf2_doc.load_page(page_number)

        # Obtener las imágenes de las páginas como matrices numpy
        pixmap1 = pdf1_page.get_pixmap(matrix=fitz.Matrix(3, 3))  # Escalar el tamaño de la imagen
        pixmap2 = pdf2_page.get_pixmap(matrix=fitz.Matrix(3, 3))  # Escalar el tamaño de la imagen

        img1 = Image.frombytes("RGB", [pixmap1.width, pixmap1.height], pixmap1.samples)
        img2 = Image.frombytes("RGB", [pixmap2.width, pixmap2.height], pixmap2.samples)

        # Convierte las imágenes en matrices numpy
        img1_np = np.array(img1)
        img2_np = np.array(img2)

        # Encuentra las diferencias entre las imágenes
        diff_img = np.abs(img1_np - img2_np)
        mask = img2_np < img1_np
        diff_img_only_img2 = diff_img.copy()
        diff_img_only_img2[~mask] = 0  # Setea a cero las diferencias que no corresponden a la imagen dos

        # Crea una nueva imagen con las diferencias resaltadas en rojo
        diff_img_pil = Image.fromarray(diff_img_only_img2.astype(np.uint8))
        diff_img_pil = diff_img_pil.convert("RGBA")
        data = diff_img_pil.getdata()
        newData = []
        for item in data:
            # Resalta solo las diferencias, manteniendo el resto transparente
            if item[0] or item[1] or item[2]:  # Si alguno de los canales R, G o B es diferente de cero
                newData.append((255, 0, 0, 255))  # Resaltado en rojo
            else:
                newData.append((0, 0, 0, 0))  # Transparente
        diff_img_pil.putdata(newData)

        # Superponer la imagen original del PDF 1 con las áreas resaltadas
        img1_pil = img1.convert("RGBA")
        img_overlay = Image.alpha_composite(img1_pil, diff_img_pil)

        # Guarda la imagen superpuesta con compresión ajustada y mayor tamaño
        img_overlay.save(output_image_path.format(page_number), format='png', quality=output_quality, dpi=(output_dpi, output_dpi))
        print(f"... Imagen de diferencias para la página {page_number} guardada en {output_image_path.format(page_number)} \u2713")

    # Cierra los documentos PDF
    pdf1_doc.close()
    pdf2_doc.close()
