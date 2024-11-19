from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import WebScraper
from analyzer import Analyzer

app = Flask(__name__)
CORS(app)


@app.route('/api/analyze', methods=['POST'])
def analyze_website():
    try:
        # Récupérer l'URL depuis la requête
        data = request.json
        url = data.get('url')
        max_elements = data.get('max_elements', 50)
        if not url:
            return jsonify({'error': 'URL manquante'}), 400

        # Initialiser le scraper et récupérer les données
        scraper = WebScraper(url, max_elements)
        if not scraper.scrape():
            return jsonify({'error': 'Échec du scraping'}), 500

        # Analyser les données avec le LLM
        analyzer = Analyzer(scraper.data)

        # Générer les résultats de l'analyse
        analysis_results = analyzer.generate_analysis()

        return jsonify(analysis_results)
    except Exception as e:
        return jsonify({
            'error': 'Erreur analyse',
            'details': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
