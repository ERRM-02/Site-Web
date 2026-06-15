import glob

for f in glob.glob('*.html'):
    if f == '404.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We replace 'Demander un devis' with 'Contactez-nous' for navbar and mobile menu
    content = content.replace('class="navbar-cta">Demander un devis</a>', 'class="navbar-cta">Contactez-nous</a>')
    content = content.replace('class="navbar-cta active">Demander un devis</a>', 'class="navbar-cta active">Contactez-nous</a>')
    # For mobile menu, it's typically: <a href="contact.html">Demander un devis</a> inside <div class="mobile-menu">
    content = content.replace('<a href="contact.html">Demander un devis</a>', '<a href="contact.html">Contactez-nous</a>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated {f}')
