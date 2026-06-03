import codecs

filepath = r"C:\Users\User\Documents\ERRM\Site web\css\style.css"

with open(filepath, 'rb') as f:
    raw_data = f.read()

# The file was originally UTF-8. The UTF-16 text was appended.
# Let's find the start of the corrupted text: "/* --- Personnalisation Tarteaucitron"
# but it was appended as UTF-16, so it starts with null bytes.

# Let's just decode ignoring errors to find where the original file ended.
# The original file ended at:
# .services-section {
#     padding-bottom: 40px !important;
# }
marker = b"padding-bottom: 40px !important;\r\n}"
idx = raw_data.find(marker)

if idx != -1:
    clean_data = raw_data[:idx + len(marker)]
    # Write back as utf-8
    with open(filepath, 'wb') as f:
        f.write(clean_data)
        
    print("Cleaned up corrupted data.")
    
    # Now append the correct CSS
    css_to_append = """

/* --- Personnalisation Tarteaucitron (Bandeau de cookies) --- */
#tarteaucitronRoot * {
    font-family: 'Poppins', sans-serif !important;
}
#tarteaucitronAlertBig {
    background: #111 !important;
    border-top: 3px solid var(--primaire) !important;
    box-shadow: 0 -10px 30px rgba(0,0,0,0.5) !important;
    color: #fff !important;
    padding: 15px 20px !important;
}
#tarteaucitronAlertBig #tarteaucitronDisclaimerAlert {
    font-size: 0.95rem !important;
    color: #ccc !important;
}
#tarteaucitronAlertBig #tarteaucitronDisclaimerAlert strong {
    color: #fff !important;
}
/* Boutons du bandeau */
#tarteaucitronAlertBig .tarteaucitronCTAButton {
    border-radius: 4px !important;
    font-weight: 600 !important;
    padding: 10px 20px !important;
    text-transform: uppercase !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    transition: all 0.3s ease !important;
}
#tarteaucitronAlertBig #tarteaucitronPersonalize {
    background: transparent !important;
    color: #fff !important;
    border: 1px solid #555 !important;
}
#tarteaucitronAlertBig #tarteaucitronPersonalize:hover {
    background: #333 !important;
}
#tarteaucitronAlertBig #tarteaucitronAllDenied {
    background: #333 !important;
    color: #fff !important;
    border: 1px solid #333 !important;
}
#tarteaucitronAlertBig #tarteaucitronAllDenied:hover {
    background: #555 !important;
}
#tarteaucitronAlertBig #tarteaucitronAllAllowed {
    background: var(--primaire) !important;
    color: #fff !important;
    border: 1px solid var(--primaire) !important;
}
#tarteaucitronAlertBig #tarteaucitronAllAllowed:hover {
    background: #a00000 !important;
}
/* Rendre le gros panneau central (si on clique sur "Personnaliser") beaucoup plus discret et stylé */
#tarteaucitron {
    max-width: 650px !important;
    border-radius: 8px !important;
    border: 1px solid #333 !important;
    background: #1a1a1a !important;
    box-shadow: 0 20px 50px rgba(0,0,0,0.8) !important;
}
#tarteaucitron .tarteaucitronTitle {
    background: #111 !important;
    color: #fff !important;
    border-bottom: 1px solid #333 !important;
    border-radius: 8px 8px 0 0 !important;
}
#tarteaucitron .tarteaucitronDetails {
    color: #ccc !important;
}
#tarteaucitron .tarteaucitronName {
    color: #fff !important;
}
"""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css_to_append)
    print("Successfully appended clean CSS.")
else:
    print("Could not find the marker!")
