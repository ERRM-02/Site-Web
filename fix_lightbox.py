import os
import re

files_to_fix = [
    r"C:\Users\User\Documents\ERRM\Site web\realisations.html",
    r"C:\Users\User\Documents\ERRM\Site web\savoir-faire.html",
    r"C:\Users\User\Documents\ERRM\Site web\index.html"
]

def replace_extension(match):
    full_str = match.group(0)
    path = match.group(1)
    if "images/realisations/" in path and not path.endswith(".jpeg"):
        return f'data-lightbox="{path}.webp"'
    return full_str

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for data-lightbox="..."
        new_content = re.sub(r'data-lightbox="([^"]+)\.(jpg|JPG|png)"', replace_extension, content)
        
        # Just in case, let's also check href="..." if it's used as a link to the image
        # (Though usually it's data-lightbox for lightboxes)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filepath}")
        else:
            print(f"No changes in {filepath}")
