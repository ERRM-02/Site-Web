import os
import glob
import re

def update_html():
    html_files = glob.glob('*.html')
    
    # Regex to find image src attributes
    img_pattern = re.compile(r'(src|href)=[\'"]([^\'"]+\.(?:jpg|JPG|png|PNG|jpeg|JPEG))[\'"]')
    # CSS background-image
    bg_pattern = re.compile(r'url\([\'"]?([^\'")]+\.(?:jpg|JPG|png|PNG|jpeg|JPEG))[\'"]?\)')

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        def replacer(match, is_bg=False):
            full_match = match.group(0)
            img_path = match.group(2) if not is_bg else match.group(1)
            
            # Check if webp version exists
            base, ext = os.path.splitext(img_path)
            webp_path = base + '.webp'
            
            # Since paths in HTML are relative to root (e.g., images/...), check if it exists on disk
            if os.path.exists(webp_path):
                print(f"[{html_file}] Replacing {img_path} -> {webp_path}")
                if not is_bg:
                    return f'{match.group(1)}="{webp_path}"'
                else:
                    return f'url({webp_path})'
            return full_match

        new_content = img_pattern.sub(lambda m: replacer(m, False), content)
        new_content = bg_pattern.sub(lambda m: replacer(m, True), new_content)

        if new_content != content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {html_file}")

if __name__ == '__main__':
    update_html()
