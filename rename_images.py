import os
import re
import urllib.parse

def slugify(text):
    text = text.lower()
    text = text.replace('é', 'e').replace('è', 'e').replace('ê', 'e')
    text = text.replace('à', 'a').replace('â', 'a')
    text = text.replace('ç', 'c')
    text = text.replace('&', 'et')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

base_dir = r"C:\Users\User\Documents\ERRM\Site web\images\realisations"
categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

for cat in categories:
    cat_path = os.path.join(base_dir, cat)
    images = [img for img in os.listdir(cat_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    images.sort()
    
    cat_slug = slugify(cat)
    
    count = 1
    for img in images:
        old_path = os.path.join(cat_path, img)
        ext = os.path.splitext(img)[1].lower()
        
        # Don't rename if it's already well named
        if img.startswith(f"{cat_slug}-errm-"):
            continue
            
        new_name = f"{cat_slug}-errm-villers-cotterets-{count}{ext}"
        new_path = os.path.join(cat_path, new_name)
        
        # Handle conflicts just in case
        while os.path.exists(new_path) and new_path != old_path:
            count += 1
            new_name = f"{cat_slug}-errm-villers-cotterets-{count}{ext}"
            new_path = os.path.join(cat_path, new_name)
            
        os.rename(old_path, new_path)
        count += 1

print("Images successfully renamed to SEO-friendly filenames.")
