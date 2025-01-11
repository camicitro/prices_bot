import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraping.changomas_scraper import ChangoMasScraper

scraper = ChangoMasScraper()
results = scraper.scrape("arroz")
print(results)
