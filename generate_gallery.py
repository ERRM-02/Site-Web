import os
import re

html_file = r"C:\Users\User\Documents\ERRM\Site web\realisations.html"
base_dir = r"C:\Users\User\Documents\ERRM\Site web\images\realisations"

categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
gallery_html = []

delay_counter = 0

for cat in sorted(categories):
    cat_path = os.path.join(base_dir, cat)
    if os.path.exists(cat_path):
        images = os.listdir(cat_path)
        for img in sorted(images):
            if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
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

# On remplace le contenu entre <div class="gallery-page-grid"> et </div>
# On utilise une expression régulière pour trouver le début et la fin
pattern = re.compile(r'(<div class="gallery-page-grid">)(.*?)(<!-- Message ajout photos -->)', re.DOTALL)

replacement = r'\1\n' + new_gallery_block.replace('\\', r'\\') + r'\n\n            </div>\n\n            \3'

new_content = pattern.sub(replacement, content)

# On va supprimer le bloc de message temporaire aussi
pattern_msg = re.compile(r'(<!-- Message ajout photos -->)(.*?)(</div>)', re.DOTALL)
new_content = pattern_msg.sub('', new_content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"[{len(gallery_html)}] photos intégrées dans la galerie.")
