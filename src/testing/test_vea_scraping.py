import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraping.vea_scraper import VeaScraper

scraper = VeaScraper()
results = scraper.scrape("Arroz")
print(results)
