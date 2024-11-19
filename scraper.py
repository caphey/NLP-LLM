import requests
from bs4 import BeautifulSoup
from datetime import datetime


class WebScraper:
    def __init__(self, url, max_elements):
        self.url = url
        self.max_elements = max_elements
        self.data = {
            "metadata": {
                "url": url,
                "date_analysis": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "max_elements": max_elements
            },
            "content": {
                "title": "",
                "headings": {
                    "h1": [],
                    "h2": [],
                    "h3": [],
                    "h4": [],
                    "h5": [],
                    "h6": []
                },
                "images": [],
                "links": [],
                "paragraphs": []
            }
        }

    def scrape(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print(f"Connexion réussie ! Status code: {
                      response.status_code}")
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extraire le titre
                self.data["content"]["title"] = soup.title.string if soup.title else "No title found"

                # Extraire tous les niveaux de titres (h1 à h6)
                for i in range(1, 7):
                    heading_tag = f'h{i}'
                    headings = soup.find_all(heading_tag)[:self.max_elements]
                    self.data["content"]["headings"][heading_tag] = [
                        h.get_text(strip=True)
                        for h in headings
                    ]
                    print(f"Nombre de {heading_tag} trouvés : {len(headings)}")

                # Extraire les liens
                self.data["content"]["links"] = [
                    {
                        "text": a.get_text(strip=True),
                        "href": a.get('href')
                    }
                    for a in soup.find_all('a')[:self.max_elements]
                ]

                # Extraire les images
                self.data["content"]["images"] = [
                    img.get('src')
                    for img in soup.find_all('img')[:self.max_elements]
                ]

                # Extraire les paragraphes
                self.data["content"]["paragraphs"] = [
                    p.get_text(strip=True)
                    for p in soup.find_all('p')[:self.max_elements]
                ]
                return self.data
            else:
                print(f"Erreur de connexion. Status code: {
                      response.status_code}")
                return False

        except Exception as e:
            print(f"Erreur : {str(e)}")
            return False