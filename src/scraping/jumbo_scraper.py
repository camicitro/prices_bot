from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys
import os
import time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from base_scraper import BaseScraper


class JumboScraper(BaseScraper):
    def scrape(self, product_name):
        base_url = f"https://www.jumbo.com.ar/{product_name}?_q={product_name}&map=ft"

        def scraping_logic(driver):
            driver.get(base_url)

            if not self.wait_for_element(driver, By.CSS_SELECTOR, "section.vtex-product-summary-2-x-container"):
                print("No se encontraron productos en la página.")
                return []
            time.sleep(3)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            products = []

            # Selección de productos
            product_items = soup.select("section.vtex-product-summary-2-x-container")
            for item in product_items:
                try:
                    name = item.select_one(".vtex-product-summary-2-x-productNameContainer span").text.strip()

                    price = item.select_one(".jumboargentinaio-store-theme-1dCOMij_MzTzZOCohX1K7w").text.strip()

                    image_url = item.select_one("img.vtex-product-summary-2-x-image")["src"]

                    product_url = "https://www.jumbo.com.ar" + item.select_one("a.vtex-product-summary-2-x-clearLink")["href"]

                    products.append({
                        "name": name,
                        "price": price,
                        "image_url": image_url,
                        "product_url": product_url,
                    })
                except AttributeError:
                    continue

            return products

        return self.with_driver(scraping_logic)