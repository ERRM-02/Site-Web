from PIL import Image
import os

img_p6_37 = r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\realisation_p6_37.jpeg"

if os.path.exists(img_p6_37):
    try:
        with Image.open(img_p6_37) as img:
            # Rotate 90 degrees clockwise
            img.rotate(-90, expand=True).save(img_p6_37)
            print("Rotated 90 degrees clockwise")
    except Exception as e:
        print(f"Error: {e}")
