from PIL import Image
import os

img_p6_37 = r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\realisation_p6_37.jpeg"
img_sam = r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Métallerie & Serrurerie\SAM_7023.webp"

if os.path.exists(img_p6_37):
    try:
        with Image.open(img_p6_37) as img:
            # We already rotated this one twice (180 total). Let's rotate 90 degrees more.
            # This puts it at 270 deg (or 90 deg counter-clockwise from the original).
            img.rotate(90, expand=True).save(img_p6_37)
    except Exception as e:
        print(f"Error {img_p6_37}: {e}")

if os.path.exists(img_sam):
    try:
        with Image.open(img_sam) as img:
            # First time rotating this one, let's try 90 deg clockwise.
            img.rotate(-90, expand=True).save(img_sam)
    except Exception as e:
        print(f"Error {img_sam}: {e}")
