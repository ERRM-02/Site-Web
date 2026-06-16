import os
import re
import urllib.parse
import html

html_file = r"C:\Users\User\Documents\ERRM\Site web\realisations.html"
sitemap_path = r"C:\Users\User\Documents\ERRM\Site web\sitemap.xml"
base_dir = r"C:\Users\User\Documents\ERRM\Site web\images\realisations"

print("--- Début de la mise à jour du site ---")

categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# --- 1. Mise à jour de la galerie (realisations.html) ---
print("\n1. Mise à jour de la galerie (realisations.html)...")
gallery_html = []
delay_counter = 0

for cat in sorted(categories):
    cat_path = os.path.join(base_dir, cat)
    if os.path.exists(cat_path):
        images = [img for img in os.listdir(cat_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        for img in sorted(images):
            img_path = f"images/realisations/{cat}/{img}"
            delay_class = f" reveal-delay-{delay_counter % 3}" if delay_counter % 3 != 0 else ""
            item_html = f"""
                <div class="gallery-page-item reveal{delay_class}" data-lightbox="{img_path}" style="cursor:pointer">
                    <img src="{img_path}" alt="{cat} — ERRM" loading="lazy" />
                    <div class="gallery-page-overlay">
                        <span>{cat}</span>
                        <h4>Réalisation ERRM</h4>
                    </div>
                </div>"""
            gallery_html.append(item_html)
            delay_counter += 1

new_gallery_block = "\n".join(gallery_html)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<div class="gallery-page-grid">)(.*?)(</div>\s*</div>\s*</section>)', re.DOTALL)
replacement = r'\1\n' + new_gallery_block.replace('\\', r'\\') + r'\n\n            \3'
new_content = pattern.sub(replacement, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f" -> [{len(gallery_html)}] photos intégrées dans la galerie.")


# --- 2. Mise à jour du sitemap (sitemap.xml) ---
print("\n2. Mise à jour du Sitemap (sitemap.xml)...")
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

image_tags = []
for cat in sorted(categories):
    cat_path = os.path.join(base_dir, cat)
    images = [img for img in os.listdir(cat_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    for img in sorted(images):
        img_url = f"https://errm.fr/images/realisations/{cat}/{img}"
        img_url = urllib.parse.quote(img_url, safe=":/") 
        img_title = f"{cat} — ERRM"
        img_title_escaped = html.escape(img_title)
        tag = f"""    <image:image>
      <image:loc>{img_url}</image:loc>
      <image:title>{img_title_escaped}</image:title>
    </image:image>"""
        image_tags.append(tag)

image_block = "\n".join(image_tags)
pattern_sitemap = re.compile(r'(<loc>https://errm\.fr/realisations</loc>.*?<priority>.*?</priority>\n)(.*?)(  </url>)', re.DOTALL)
match = pattern_sitemap.search(sitemap_content)

if match:
    new_sitemap_content = sitemap_content[:match.start(2)] + image_block + "\n" + match.group(3) + sitemap_content[match.end(3):]
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_sitemap_content)
    print(f" -> Sitemap mis à jour avec {len(image_tags)} images.")
else:
    print(" -> Erreur : Impossible de trouver le bloc realisations.html dans le sitemap.")

print("\n--- Mise à jour terminée avec succès ! ---")
