
# Allo!Asso — Plateforme de dons pour associations

Allo!Asso est une application web conçue pour faciliter les dons aux associations. Elle offre un système d'inscription, de connexion et de gestion de dons, avec une base de données MySQL intégrée. Le projet est développé avec **Flask** (Python) et structuré pour être déployé facilement sur **Render.com** ou exécuté localement.

---

## Fonctionnalités

- Création de compte sécurisé (mot de passe haché)
- Connexion et session utilisateur
- Formulaire de don avec choix du moyen de paiement
- Interface responsive avec menu hamburger
- Backend connecté à MySQL (local ou cloud)
- Déploiement simple sur Render

---

## Structure du projet

alloasso/
│
├── app.py                  # Application Flask principale
├── templates/              # Fichiers HTML (pages du site)
├── static/                 # CSS, JavaScript
├── schema.sql              # Script SQL de création des tables
├── .env                    # Variables d'environnement (config MySQL)
│
├── requirements.txt        # Dépendances Python
├── Procfile                # Pour déploiement sur Render
├── runtime.txt             # Version de Python
└── README.md               # Ce fichier

---

## Prérequis

- Python 3.10 ou supérieur
- MySQL (local ou distant)
- pip (gestionnaire de paquets Python)

---

## Installation locale

1. **Cloner le projet ou extraire le `.zip`**

2. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données**

   - Créer une base MySQL nommée `alloasso` (ou autre)
   - Importer le fichier `schema.sql`
   - Modifier le fichier `.env` :
     ```
     DB_HOST=localhost
     DB_USER=ton_utilisateur
     DB_PASSWORD=ton_mot_de_passe
     DB_NAME=alloasso
     ```

5. **Lancer l’application**
   ```bash
   python app.py
   ```

6. **Accéder à l'application**
   - Ouvrir [http://127.0.0.1:5000](http://127.0.0.1:5000) dans ton navigateur

---

## Déploiement sur Render

1. Créer un compte sur [render.com](https://render.com)
2. Cliquer sur **"New Web Service"**
3. Uploader ce projet ou connecter ton repo GitHub
4. Render détecte automatiquement Flask via le `Procfile`
5. Ajouter tes variables d’environnement MySQL dans Render
6. Cliquer sur **"Deploy"** et c’est en ligne !

---

## Variables d’environnement requises (`.env`)

```
SECRET_KEY=une_clé_ultra_secrète
DB_HOST=localhost
DB_USER=ton_utilisateur
DB_PASSWORD=ton_mot_de_passe
DB_NAME=alloasso
```

---

## À venir

- Tableau de bord des dons par utilisateur
- Paiements en ligne (via Stripe ou PayPal)
- Zone d’administration
- Page publique pour chaque association

---

## Auteurs

Développé avec passion par ROMARIC MFUMU et assisté par ChatGPT.  
Projet librement modifiable pour toutes vos idées associatives.

---

## Licence

Ce projet est open source et libre d’utilisation. N’hésitez pas à le forker !
