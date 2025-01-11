import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraping.jumbo_scraper import JumboScraper

scraper = JumboScraper()
results = scraper.scrape("Arroz")
print(results)
