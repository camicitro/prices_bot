import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraping.carrefour_scraper import CarrefourScraper

scraper = CarrefourScraper()
results = scraper.scrape("smart tv")
print(results)
