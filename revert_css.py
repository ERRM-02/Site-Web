import os

filepath = r"C:\Users\User\Documents\ERRM\Site web\css\style.css"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

marker = "/* --- Personnalisation Tarteaucitron"

if marker in content:
    clean_content = content.split(marker)[0]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(clean_content.rstrip() + "\n")
    print("Reverted Tarteaucitron custom styles.")
else:
    print("Marker not found.")
