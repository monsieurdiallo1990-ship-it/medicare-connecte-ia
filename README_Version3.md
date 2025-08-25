# Medicare Connect – Prototype rapide avec IA médicale

Ce projet vous permet de :
- Visualiser et filtrer un fichier CSV de demandes médicales ou patients.
- Discuter avec un assistant médical IA (OpenAI GPT) pour poser des questions ou obtenir des conseils généraux.
- Obtenir une suggestion IA sur les besoins médicaux décrits dans le fichier CSV.

## Installation et lancement

1. **Installez Python 3.8 ou supérieur.**
2. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```
3. **Lancez l’application :**
   ```bash
   streamlit run app.py
   ```
4. **Ouvrez l’interface web (le lien s’affiche dans le terminal).**
5. **Téléchargez votre fichier CSV via l’interface.**
6. **Pour utiliser l’IA, obtenez une clé API OpenAI sur https://platform.openai.com/api-keys et renseignez-la dans le champ prévu.**

## Fonctionnalités

- Upload et filtrage de CSV
- Assistant IA médical (discussion, conseils généraux)
- Suggestion IA à partir des besoins des patients
- Export des résultats filtrés

## Sécurité & Confidentialité

- **Les réponses de l’IA sont informatives et ne remplacent jamais un avis médical professionnel.**
- **Ne partagez pas d’informations sensibles sans précaution.**

## Hébergement

Ce prototype peut être hébergé simplement sur [Streamlit Cloud](https://streamlit.io/cloud), Render, ou Hugging Face Spaces.

---

*Pour des fonctionnalités avancées (authentification, notifications, gestion multi-utilisateurs), contactez un développeur pour faire évoluer ce prototype.*