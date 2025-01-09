import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraping.changomas_scraper import ChangoMasScrapper

scraper = ChangoMasScrapper()
results = scraper.scrape("arroz")
print(results)
