# Projet : Analyseur Web IA

Ce projet vise à analyser des sites web en utilisant des techniques de traitement du langage naturel (NLP) et des modèles de langage de grande taille (LLM). Il fournit des analyses détaillées sur les performances, le SEO, le contenu et l'expérience utilisateur.

<video width="auto" height="240" controls>
  <source src="website-analyzer/public/record_home.mp4">
  Your browser does not support the video tag.
</video>



## 📋 Table des matières

- [🎯 Objectifs du projet](#🎯-objectifs-du-projet)
- [🏗 Architecture technique](#🏗-architecture-technique)
- [💻 Installation](#💻-installation)
- [🚀 Fonctionnalités principales](#🚀-fonctionnalités-principales)
- [📊 Analyses disponibles](#📊-analyses-disponibles)
- [🔧 API et intégrations](#🔧-api-et-intégrations)
- [🤖 Utilisation des LLM](#🤖-utilisation-des-llm)
- [📝 Rapport d'analyse](#📝-rapport-danalyse)
- [⚙️ Configuration avancée](#⚙️-configuration-avancée)
- [🔍 Tests et validation](#🔍-tests-et-validation)
- [📚 Ressources additionnelles](#📚-ressources-additionnelles)
- [🤝 Contribution](#🤝-contribution)

## 🎯 Objectifs du projet

- Analyser les performances des sites web.
- Évaluer le SEO et le contenu des pages.
- Fournir des insights sur l'expérience utilisateur (UX/UI).
- Utiliser des modèles de langage avancés pour des analyses approfondies.

## 🏗 Architecture technique

- **Stack technologique** : Python, Flask, React, BeautifulSoup4, Ollama

- **Composants principaux** :
- Interface utilisateur (React)
- API backend (Flask)
- Scraper web (BeautifulSoup4)
- Analyseur (Ollama, Llama, Moondream)

- **Intégrations** :

  - Ollama pour les LLM

- **Fichiers de l'espace de travail** :
  - `README.md`
  - `app.py`
  - `scraper.py`
  - `analyzer.py`
  - `website-analyzer/src/App.jsx`
  - `website-analyzer/src/components/*`

## 💻 Installation

### Prérequis

- Python 3.8+
- Node.js 14+
- npm
- React
- TailwindCSS

## 🚀 Fonctionnalités principales

- **Analyse SEO**

- **Analyse de contenu NLP**
- **Analyse des performances**

- **Analyse UX/UI**

## 📊 Analyses disponibles

### Analyse SEO

- Vérification des balises méta
- Analyse des mots-clés

### Analyse de contenu NLP

- Extraction des entités nommées
- Analyse de sentiment

### Analyse des performances

- Temps de chargement des pages
- Utilisation des ressources

### Analyse UX/UI

- Évaluation de la structure des titres
- Analyse de la densité des liens et des images

## 🔧 API et intégrations

### Endpoints

- **POST /api/analyze** : Analyse un site web
  ```json
  {
    "url": "https://example.com",
    "max_elements": 50
  }
  ```

## 🤖 Utilisation des LLM

### Modèles utilisés

- Ollama pour les LLM

### Cas d'usage

- Génération de résumés
- Analyse des images

### Exemples de prompts

```python
prompt = "Analyse le contenu de cette page web et donne un résumé."
```

## 📝 Rapport d'analyse

### Structure

- Introduction
- Résultats des analyses
- Recommandations

## ⚙️ Configuration avancée

- Options de personnalisation des analyses
- Paramètres de scraping

## 🔍 Tests et validation

### Procédures de test

- Tests unitaires
- Tests d'intégration

### Métriques de qualité

- Couverture de code
- Performances des analyses

## 📚 Ressources additionnelles

- [Documentation BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Documentation Ollama](https://github.com/ollama/ollama)
- [Documentation Moondream](https://github.com/vikhyat/moondream)

## 🤝 Contribution

- Milane AUTOUR
- Hicham LATRECHE
- Adlan HAMLA
- Amir LABIDI
- Mohammed-Medhi MILOUA
