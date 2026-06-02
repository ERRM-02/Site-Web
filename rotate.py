from PIL import Image
import os

img1 = r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\realisation_p6_37.jpeg"
img2 = r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie\realisation_p6_38.jpeg"

if os.path.exists(img1):
    with Image.open(img1) as im:
        # Walkway sideways - rotate 90 degrees clockwise (-90)
        im.rotate(-90, expand=True).save(img1)
        print("Rotated p6_37 clockwise")

if os.path.exists(img2):
    with Image.open(img2) as im:
        # Stairs sideways - rotate 90 degrees counter-clockwise (90)
        im.rotate(90, expand=True).save(img2)
        print("Rotated p6_38 counter-clockwise")
