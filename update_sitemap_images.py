import os
import re
import xml.etree.ElementTree as ET

sitemap_path = r"C:\Users\User\Documents\ERRM\Site web\sitemap.xml"
base_dir = r"C:\Users\User\Documents\ERRM\Site web\images\realisations"

with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

image_tags = []
for cat in sorted(categories):
    cat_path = os.path.join(base_dir, cat)
    images = [img for img in os.listdir(cat_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    for img in sorted(images):
        img_url = f"https://errm.fr/images/realisations/{cat}/{img}".replace(" ", "%20")
        img_title = f"{cat} — ERRM"
        tag = f"""    <image:image>
      <image:loc>{img_url}</image:loc>
      <image:title>{img_title}</image:title>
    </image:image>"""
        image_tags.append(tag)

image_block = "\n".join(image_tags)

# Find the realisations.html url block and replace or inject the images
pattern = re.compile(r'(<loc>https://errm\.fr/realisations\.html</loc>.*?<priority>.*?</priority>\n)(.*?)(  </url>)', re.DOTALL)

# Remove old image tags if they exist
match = pattern.search(sitemap_content)
if match:
    new_content = sitemap_content[:match.start(2)] + image_block + "\n" + match.group(3) + sitemap_content[match.end(3):]
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Sitemap updated with image tags.")
else:
    print("Could not find realisations.html block in sitemap.")
