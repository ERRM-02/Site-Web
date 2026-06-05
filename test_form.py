import urllib.request
import urllib.parse
import json

url = "https://formspree.io/f/xlgkdvyn"
data = urllib.parse.urlencode({
    "email": "test@errm.fr",
    "message": "Ceci est un test automatique du site web."
}).encode('utf-8')

req = urllib.request.Request(url, data=data, headers={
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Origin': 'https://errm.fr',
    'Referer': 'https://errm.fr/contact.html'
})

try:
    with urllib.request.urlopen(req) as response:
        print("Status Code:", response.getcode())
        print("Response:", response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("Error:", getattr(e, 'code', e.reason))
    try:
        print("Body:", e.read().decode('utf-8'))
    except:
        pass
