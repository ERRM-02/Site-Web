import os
import glob
import re

html_files = glob.glob('*.html')
xml_files = glob.glob('sitemap.xml')

# Files to process
files_to_process = html_files + xml_files

# The extensions we want to strip from the href/url strings
# Be careful not to replace external links ending in .html (if any, though unlikely to be our internal ones)
internal_pages = ['a-propos', 'contact', 'realisations', 'savoir-faire', 'mentions-legales', 'index', 'merci']

def replace_links(content):
    # Replace in href="..."
    for page in internal_pages:
        if page == 'index': continue # typically we link to / not index.html, but just in case
        
        # basic href
        content = content.replace(f'href="{page}.html"', f'href="{page}"')
        content = content.replace(f"href='{page}.html'", f"href='{page}'")
        
        # with query params
        content = content.replace(f'href="{page}.html?', f'href="{page}?')
        content = content.replace(f"href='{page}.html?", f"href='{page}?")
        
        # absolute URLs (og:url, canonical, sitemap)
        content = content.replace(f'https://errm.fr/{page}.html', f'https://errm.fr/{page}')
        
        # JS references (if any)
        content = content.replace(f'"{page}.html"', f'"{page}"')
        content = content.replace(f"'{page}.html'", f"'{page}'")
        
    return content

for f in files_to_process:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    new_content = replace_links(content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
    else:
        print(f'No changes in {f}')
