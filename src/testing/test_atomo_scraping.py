import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraping.atomo_scraper import AtomoScraper

scraper = AtomoScraper()
results = scraper.scrape("Arroz")
print(results)
