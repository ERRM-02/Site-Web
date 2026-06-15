import os

files = ['index.html', 'a-propos.html', 'contact.html', 'realisations.html', 'savoir-faire.html', 'mentions-legales.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<link rel="canonical"' not in content:
        url = 'https://errm.fr/' if f == 'index.html' else f'https://errm.fr/{f}'
        canonical_tag = f'    <link rel="canonical" href="{url}" />\n'
        
        # Insert before <link rel="icon"
        if '<link rel="icon"' in content:
            content = content.replace('<link rel="icon"', canonical_tag + '    <link rel="icon"')
        else:
            content = content.replace('</head>', canonical_tag + '</head>')
            
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Added canonical to {f}')
    else:
        print(f'{f} already has canonical')
