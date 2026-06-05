from PIL import Image
import os

png_path = r"C:\Users\User\Documents\ERRM\Site web\images\Interieur_de_l'atelier_modif.png"
webp_path = r"C:\Users\User\Documents\ERRM\Site web\images\interieur-atelier.webp"

if os.path.exists(png_path):
    print("Converting...")
    with Image.open(png_path) as im:
        # Save as webp
        im.save(webp_path, "WEBP", quality=80)
    print(f"Saved to {webp_path}")
else:
    print("PNG file not found.")
