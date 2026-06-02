import os
from PIL import Image

dirs = [
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Chaudronnerie & Tuyauterie",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Charpente Métallique",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Maintenance industrielle",
    r"C:\Users\User\Documents\ERRM\Site web\images\realisations\Métallerie & Serrurerie"
]

for d in dirs:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            path = os.path.join(d, f)
            try:
                with Image.open(path) as img:
                    w, h = img.size
                    print(f"{f}: {w}x{h}")
            except Exception as e:
                pass
