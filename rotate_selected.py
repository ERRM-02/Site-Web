from PIL import Image, ImageOps
import os

files = [
    r"C:\Users\User\Documents\ERRM\Site web\images\20200527_135541.webp",
    r"C:\Users\User\Documents\ERRM\Site web\images\20220311_105756.webp",
    r"C:\Users\User\Documents\ERRM\Site web\images\20250925_165507.webp",
    r"C:\Users\User\Documents\ERRM\Site web\images\real-coffret.webp",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\20250117_144903.webp",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\realisation_p6_37.jpeg",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\realisation_p6_38.jpeg",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\WP_20220212_19_50_29_Pro.webp",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\WP_20220212_19_50_57_Pro.webp"
]

for f in files:
    if os.path.exists(f):
        try:
            with Image.open(f) as img:
                # First try to strip EXIF if it's interfering, or just rotate.
                # We will just rotate 90 degrees clockwise.
                rotated = img.rotate(-90, expand=True)
                rotated.save(f)
                print(f"Rotated {os.path.basename(f)} by 90 degrees clockwise.")
        except Exception as e:
            print(f"Error processing {f}: {e}")
    else:
        print(f"File not found: {f}")
