from scraping.jumbo_scraper import JumboScraper
from scraping.atomo_scraper import AtomoScraper
from scraping.carrefour_scraper import CarrefourScraper
from scraping.changomas_scraper import ChangoMasScrapper
from scraping.coto_scraper import CotoScraper
from scraping.vea_scraper import VeaScraper

class ScraperFactory:
    @staticmethod
    def get_scraper(supermarket):
        scrapers = {
            "jumbo": JumboScraper,
            "atomo": AtomoScraper,
            "carrefour": CarrefourScraper,
            "changomas": ChangoMasScrapper,
            "coto": CotoScraper,
            "vea": VeaScraper,
            
        }
        scraper_class = scrapers.get(supermarket.lower())
        if scraper_class:
            return scraper_class()
        else:
            raise ValueError(f"Scraper no encontrado para el supermercado: {supermarket}")

