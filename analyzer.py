import ollama
import sys
from typing import Dict, List
from datetime import datetime
import requests
from io import BytesIO
from PIL import Image
import base64


class Analyzer:
    def __init__(self, data: dict, text_model: str = "llama3.2:1b", image_model: str = "moondream"):
        """
        Initialise l'analyseur avec les modèles spécifiés
        """
        self.text_model = text_model
        self.image_model = image_model
        self.data = data
        self.report_sections = []

        print(f"Initialisation de l'analyse avec {self.text_model} pour le texte et {
              self.image_model} pour les images...")

        # Test de connexion avec les modèles
        try:
            print("Test de connexion aux modèles...")
            ollama.chat(model=self.text_model, messages=[
                {"role": "user", "content": "test"}
            ])
            ollama.chat(model=self.image_model, messages=[
                {"role": "user", "content": "test"}
            ])
            print("Connexion réussie !")
        except Exception as e:
            print(f"\nErreur de connexion aux modèles:")
            print(str(e))
            sys.exit(1)

    def download_and_encode_image(self, url) -> str:
        """
        Télécharge une image depuis une URL et la convertit en base64
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode()
        except Exception as e:
            print(f"Erreur lors du téléchargement de l'image {url}: {str(e)}")
            return None

    def analyze_images(self) -> str:
        """Analyse des images du site"""
        print("Analyse des images en cours...")

        # Filtrer les URLs d'images valides
        valid_images = [img for img in self.data["content"]
                        ["images"] if img.startswith('http')]

        if not valid_images:
            return "Aucune image valide trouvée pour l'analyse."

        # Sélectionner un sous-ensemble d'images pour l'analyse
        selected_images = valid_images[:5]  # Limiter à 5 images pour l'exemple

        all_image_analyses = []
        for img_url in selected_images:
            try:
                # Télécharger et encoder l'image
                img_base64 = self.download_and_encode_image(img_url)
                if not img_base64:
                    continue

                # Méthode alternative d'analyse d'image
                try:
                    # Première tentative avec base64 directement
                    response = ollama.chat(model=self.image_model, messages=[
                        {"role": "user", "content": img_base64}
                    ])
                except:
                    # Si ça ne marche pas, essayer avec le format base64 URI
                    try:
                        image_uri = f"data:image/jpeg;base64,{img_base64}"
                        response = ollama.chat(model=self.image_model, messages=[
                            {"role": "user", "content": image_uri}
                        ])
                    except:
                        # Si toujours pas, essayer avec une requête simple
                        response = ollama.chat(model=self.image_model, messages=[
                            {"role": "user", "content": f"Analyze this image: {img_url}"}
                        ])

                # Ajouter une demande d'analyse spécifique après que l'image est chargée
                if response:
                    analysis_prompt = """Décris cette image en détail en te concentrant sur ses aspects marketing et son 
                    impact visuel. Analyse son style, sa composition et son message.
                    
                    Décris cette image en détail en te concentrant sur :
                    - Son style visuel
                    - Sa composition
                    - Son message marketing
                    - Son impact potentiel sur l'audience
                    
                    Utilise des phrases complètes sans puces ni tirets.
                    """
                    detailed_response = ollama.chat(model=self.image_model, messages=[
                        {"role": "user", "content": analysis_prompt}
                    ])
                    all_image_analyses.append(
                        detailed_response['message']['content'])

            except Exception as e:
                print(f"Erreur lors de l'analyse de l'image {
                      img_url}: {str(e)}")
                continue

        # Générer une analyse globale des images avec le modèle de texte
        if all_image_analyses:
            images_summary_prompt = f"""En tant qu'expert en marketing digital, analyse ces descriptions d'images du site:

            Descriptions des images:
            {' '.join(all_image_analyses)}

            Génère une analyse globale en français qui évalue:
            1. La cohérence visuelle
            2. L'impact marketing
            3. Le storytelling visuel
            4. Les recommandations d'amélioration

            Important :
            - Utilise des paragraphes complets
            - Évite les listes à puces et les tirets
            - Structure ton texte avec des sous-titres en gras
            """

            response = ollama.chat(model=self.text_model, messages=[
                {"role": "user", "content": images_summary_prompt}
            ])
            return response['message']['content']
        else:
            return "Aucune analyse d'image n'a pu être générée."

    def analyze_seo_technique(self) -> str:
        """Analyse technique SEO de la page"""
        print("Analyse SEO technique en cours...")

        title = self.data["content"]["title"]
        hs = self.data["content"]["headings"]

        prompt = f"""En tant qu'expert SEO, analyse ces éléments d'une page web:

        Titre: {title}
        H1: {hs['h1']}
        H2: {hs['h2']}
        H3: {hs['h3']}
        H4: {hs['h4']}
        H5: {hs['h5']}
        H6: {hs['h6']}

        Génère une analyse SEO détaillée en français qui couvre:
        1. La qualité et pertinence du titre
        2. La structure hiérarchique des titres
        3. Les mots-clés principaux identifiés
        4. Les recommandations d'amélioration

        Important :
        - Utilise des paragraphes complets
        - Évite les listes à puces et les tirets
        - Structure ton texte avec des sous-titres en gras

        """

        response = ollama.chat(model=self.text_model, messages=[
            {"role": "user", "content": prompt}
        ])
        return response['message']['content']

    def analyze_contenu_marketing(self) -> str:
        """Analyse du contenu marketing"""
        print("Analyse du contenu marketing...")

        paragraphs = [p for p in self.data["content"]
                      ["paragraphs"] if len(p) > 30]

        prompt = f"""En tant qu'expert marketing, analyse ce contenu du site:

        Contenu principal:
        {' '.join(paragraphs)}

        Génère une analyse marketing détaillée en français qui évalue:
        1. La proposition de valeur
        2. Les arguments de vente
        3. Le ton et le style
        4. Les points d'amélioration

        Important :
        - Utilise des paragraphes complets
        - Évite les listes à puces et les tirets
        - Structure ton texte avec des sous-titres en gras

        """

        response = ollama.chat(model=self.text_model, messages=[
            {"role": "user", "content": prompt}
        ])
        return response['message']['content']

    def analyze_user_experience(self) -> str:
        """Analyse de l'expérience utilisateur"""
        print("Analyse de l'expérience utilisateur...")

        links = self.data["content"]["links"]
        images = [img for img in self.data["content"]["images"] if img]

        prompt = f"""En tant qu'expert UX, analyse ces éléments du site:

        Navigation: {len(links)} liens
        Médias: {len(images)} images

        Principaux liens de navigation:
        {[link["text"] for link in links if link["text"]]}

        Génère une analyse UX détaillée en français qui évalue:
        1. La structure de navigation
        2. L'utilisation des médias
        3. Les points de conversion
        4. Les recommandations d'amélioration

        Important :
        - Utilise des paragraphes complets
        - Évite les listes à puces et les tirets
        - Structure ton texte avec des sous-titres en gras

        """

        response = ollama.chat(model=self.text_model, messages=[
            {"role": "user", "content": prompt}
        ])
        return response['message']['content']

    def generate_recommendations(self) -> str:
        """Génère des recommandations globales"""
        print("Génération des recommandations finales...")

        prompt = f"""En te basant sur les analyses précédentes du site, génère:

        1. Un résumé des points forts du site
        2. Les 5 recommandations prioritaires d'amélioration
        3. Une conclusion générale

        Important :
        - Utilise des paragraphes complets
        - Évite les listes à puces et les tirets
        - Structure ton texte avec des sous-titres en gras
        """

        response = ollama.chat(model=self.text_model, messages=[
            {"role": "user", "content": prompt}
        ])
        return response['message']['content']

    def calculate_kpi_scores(self) -> dict:
        """Calcul des scores KPI"""
        print("Calcul des scores KPI...")

        # Données pour l'analyse
        link_count = len(self.data['content']['links'])
        image_count = len(self.data['content']['images'])
        titles = self.data['content']['headings']

        # Calcul initial des scores basé sur des métriques simples
        performance_score = self._calculate_performance_score(
            link_count, image_count)
        ux_score = self._calculate_ux_score(link_count, image_count, titles)
        marketing_score = self._calculate_marketing_score(
            titles, self.data['content'].get('paragraphs', []))

        # Construction du dictionnaire de scores
        scores = {
            "performance": performance_score,
            "performance_label": self._get_score_label(performance_score, "Performance"),
            "ux": ux_score,
            "ux_label": self._get_score_label(ux_score, "UX"),
            "marketing": marketing_score,
            "marketing_label": self._get_score_label(marketing_score, "Marketing")
        }

        return scores

    def _calculate_performance_score(self, link_count, image_count) -> int:
        """Calcule le score de performance technique"""
        # Logique simplifiée pour l'exemple
        base_score = 50
        if link_count < 15:
            base_score += 10
        if image_count < 15:
            base_score += 5
        return min(100, max(0, base_score))

    def _calculate_ux_score(self, link_count, image_count, titles) -> int:
        """Calcule le score d'expérience utilisateur"""
        base_score = 50
        if titles.get('h1'):
            base_score += 5
        if titles.get('h2'):
            base_score += 5
        if image_count > 10:
            base_score += 10
        if 5 <= link_count <= 20:
            base_score += 10
        if image_count > 0 and link_count > 0:
            base_score += 5
        return min(100, max(0, base_score))

    def _calculate_marketing_score(self, titles, paragraphs) -> int:
        """Calcule le score marketing"""
        base_score = 50
        if titles.get('h1') and any(len(p) > 100 for p in paragraphs):
            base_score += 10
        if len(paragraphs) > 5:
            base_score += 5
        return min(100, max(0, base_score))

    def _get_score_label(self, score, category) -> str:
        """Retourne un label descriptif basé sur le score"""
        if score >= 90:
            return f"Excellent {category}"
        elif score >= 80:
            return f"Très bon {category}"
        elif score >= 70:
            return f"Bon {category}"
        elif score >= 60:
            return f"{category} correct"
        else:
            return f"{category} à améliorer"

    def generate_analysis(self) -> dict:
        print("Génération de l'analyse complète...")
        """Génère l'analyse complète et retourne les résultats"""
        try:
            # Exécution des analyses
            seo_analysis = self.analyze_seo_technique()
            content_analysis = self.analyze_contenu_marketing()
            ux_analysis = self.analyze_user_experience()
            image_analysis = self.analyze_images()
            recommendations = self.generate_recommendations()
            try:
                # Calcul des KPIs pour détecter rapidement les erreurs potentielles
                kpi_scores = self.calculate_kpi_scores()
                if not kpi_scores:
                    raise Exception("Échec du calcul des KPIs")
            except Exception as e:
                print(f"Erreur lors de la génération des analyses: {str(e)}")

            # Structure du rapport
            report = {
                "metadata": {
                    "date_analysis": self.data['metadata']['date_analysis'],
                    "url": self.data['metadata']['url'],
                    "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                },
                "kpi_overview": {
                    "performance": {
                        "score": kpi_scores["performance"],
                        "label": kpi_scores["performance_label"]
                    },
                    "user_experience": {
                        "score": kpi_scores["ux"],
                        "label": kpi_scores["ux_label"]
                    },
                    "marketing": {
                        "score": kpi_scores["marketing"],
                        "label": kpi_scores["marketing_label"]
                    }
                },
                "detailed_analysis": {
                    "seo_technique": {
                        "title": "Analyse SEO Technique",
                        "content": seo_analysis
                    },
                    "contenu_marketing": {
                        "title": "Analyse du Contenu Marketing",
                        "content": content_analysis
                    },
                    "experience_utilisateur": {
                        "title": "Analyse de l'Expérience Utilisateur",
                        "content": ux_analysis
                    },
                    "analyse_images": {
                        "title": "Analyse des Images",
                        "content": image_analysis
                    },
                    "recommendations": {
                        "title": "Recommandations",
                        "content": recommendations
                    }
                }
            }

            return report

        except Exception as e:
            print(f"Erreur lors de l'analyse : {str(e)}")
            raise Exception(f"Erreur lors de l'analyse : {str(e)}")
