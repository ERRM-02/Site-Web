# Site Web ERRM

Site statique HTML/CSS pour **ERRM** — Maintenance industrielle, chaudronnerie, tuyauterie, métallerie et serrurerie à Villers-Cotterêts.

---

## 📁 Structure du projet

```
Site web/
├── index.html            — Page d'accueil
├── savoir-faire.html     — Nos métiers (4 domaines)
├── realisations.html     — Galerie de réalisations
├── a-propos.html         — L'entreprise
├── contact.html          — Formulaire de devis
├── mentions-legales.html — Mentions légales
├── css/
│   └── style.css         — Feuille de style principale
├── js/
│   └── main.js           — Scripts (navbar, animations, lightbox)
└── images/
    ├── logo-errm.png     — Logo principal
    ├── hero-bg.jpg       — Image de fond accueil
    ├── real-escalier.jpg — Réalisation escalier
    ├── real-coffret.jpg  — Réalisation coffret acier
    └── real-cloison.jpg  — Réalisation cloison grillage
```

---

## 📬 Activer le formulaire de devis (Formspree)

Le formulaire de contact utilise **[Formspree](https://formspree.io)** pour envoyer les demandes de devis par email sans serveur.

### Étape 1 — Créer votre compte Formspree

1. Allez sur [formspree.io](https://formspree.io)
2. Créez un compte avec l'adresse email où vous souhaitez recevoir les devis
3. Créez un **nouveau formulaire** (bouton "+ New Form")
4. Notez votre **endpoint** : `https://formspree.io/f/XXXXXXXX`

### Étape 2 — Renseigner l'ID dans le code

Ouvrez `contact.html` et recherchez la ligne :

```html
<form id="contact-form" action="https://formspree.io/f/VOTRE_ID_FORMSPREE" method="POST">
```

Remplacez `VOTRE_ID_FORMSPREE` par votre vrai ID :

```html
<form id="contact-form" action="https://formspree.io/f/abcdefgh" method="POST">
```

### Étape 3 — Autoriser votre domaine sur Formspree

Dans votre tableau de bord Formspree → paramètres du formulaire → **"Allowed Domains"** :
- Ajoutez votre nom de domaine (ex : `www.errm-btp.fr`)
- Ajoutez aussi `yourusername.github.io` pour les tests

> ⚠️ **Note sur la confidentialité de l'ID**
>
> Dans un site HTML statique, l'ID Formspree est visible dans le code source de la page — **c'est normal et attendu** par Formspree. Il n'est pas possible de le cacher sans étape de build (Next.js, Vite, etc.).
>
> Formspree protège votre formulaire par d'autres moyens :
> - Restriction par domaine autorisé (paramètres du formulaire)
> - Filtre anti-spam intégré
> - Champ honeypot anti-bot déjà intégré dans le formulaire
>
> L'ID seul ne suffit pas à abuser du formulaire si votre domaine est restreint.

---

## 🌐 Déploiement sur GitHub Pages

### 1. Créer le dépôt GitHub

```bash
git init
git add .
git commit -m "Initial commit — site ERRM"
git remote add origin https://github.com/VOTRE_COMPTE/errm-site.git
git push -u origin main
```

### 2. Activer GitHub Pages

1. Sur GitHub, allez dans **Settings → Pages**
2. Source : `Deploy from a branch` → branche `main` → dossier `/ (root)`
3. Cliquez **Save**

Le site sera accessible à : `https://VOTRE_COMPTE.github.io/errm-site/`

### 3. Ajouter votre nom de domaine personnalisé

1. Dans **Settings → Pages → Custom domain** : entrez votre domaine (ex : `www.errm-btp.fr`)
2. Chez votre registrar DNS, ajoutez un enregistrement **CNAME** :
   - Nom : `www`
   - Valeur : `VOTRE_COMPTE.github.io`
3. Si vous voulez l'apex (`errm-btp.fr` sans www), ajoutez 4 enregistrements **A** pointant vers :
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
4. Cochez **"Enforce HTTPS"** dans GitHub Pages (disponible après quelques minutes)

---

## 🔄 Mettre à jour le site

```bash
# Après modification des fichiers :
git add .
git commit -m "Description de la modification"
git push
```

GitHub Pages se met à jour automatiquement dans les 1-2 minutes.

---

## 📞 Contacts

| Rôle | Nom | Téléphone |
|---|---|---|
| Standard | — | 03 23 96 77 07 |
| Commercial | Florent Langrené | 06 08 81 34 58 |
| Technique | Kévin Gay | 06 37 07 83 75 |

**Adresse** : 19 bis rue du Marchoix, 02600 Villers-Cotterêts
