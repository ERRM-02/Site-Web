import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove " Qualification QUALIBAT." from footer-desc
    content = content.replace(" Qualification QUALIBAT.", "")

    # 2. Remove the two footer-contact-items from the first column.
    content = re.sub(
        r'<div class="footer-contact-item">.*?19 Bis Rue du Marchois.*?</div>\s*<div class="footer-contact-item">.*?03 23 96 77 07.*?</div>',
        '', content, flags=re.DOTALL
    )

    # 3. Replace the Contacts directs column content
    new_contacts = '''<h4 class="footer-heading">Contacts directs</h4>
                    <div style="font-size:.88rem;color:rgba(180,190,205,0.75);line-height:2">
                        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
                            <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <circle cx="12" cy="11" r="3" />
                            </svg>
                            19 Bis Rue du Marchois, 02600 Villers-Cotterêts
                        </div>
                        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
                            <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                            </svg>
                            <a href="tel:0323967707" style="color:var(--rouge)">03 23 96 77 07</a>
                        </div>
                        <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px">
                            <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                            <a href="mailto:contact@errm.fr" style="color:var(--rouge)">contact@errm.fr</a>
                        </div>
                        <div style="color:rgba(168,168,168,0.5)">Lun–Ven 8h–17h</div>
                    </div>'''
                    
    content = re.sub(
        r'<h4 class="footer-heading">Contacts directs</h4>\s*<div style="font-size:\.88rem;color:rgba\(180,190,205,0\.75\);line-height:2">.*?Lun–Ven 8h–17h</div>\s*</div>',
        new_contacts, content, flags=re.DOTALL
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
