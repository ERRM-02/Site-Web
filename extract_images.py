import fitz
import os

pdf_path = r"U:\Administratif\Renseignements administratif pour clients\Archive plaquette\Plaquette ERRM\ERRM Presentation.pdf"
output_dir = r"C:\Users\User\Documents\ERRM\Site web\images\realisations"

os.makedirs(output_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    img_count = 0
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            img_count += 1
            image_filename = os.path.join(output_dir, f"realisation_p{page_index+1}_{img_count}.{image_ext}")
            with open(image_filename, "wb") as f:
                f.write(image_bytes)
    print(f"Extraction terminée. {img_count} images extraites dans {output_dir}")
except Exception as e:
    print(f"Erreur : {e}")
