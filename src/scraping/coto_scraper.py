from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys
import os
import time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from base_scraper import BaseScraper


class CotoScraper(BaseScraper):
    def scrape(self, product_name):
        base_url = f"https://www.cotodigital.com.ar/sitios/cdigi/categoria?_dyncharset=utf-8&Dy=1&Ntt={product_name}"

        def scraping_logic(driver):
            driver.get(base_url)

            if not self.wait_for_element(driver, By.CSS_SELECTOR, "div.producto-card"):
                print("No se encontraron productos en la página.")
                return []
            time.sleep(3)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            products = []

            # Selección de productos
            product_items = soup.select("div.producto-card")
            for item in product_items:
                try:
                    name = item.select_one(".nombre-producto").text.strip()

                    price = item.select_one(".card-title.text-center.mt-1").text.strip()

                    image_url = item.select_one("img.product-image")["src"]

                    product_url = f"https://www.cotodigital.com.ar/sitios/cdigi/categoria?_dyncharset=utf-8&Dy=1&Ntt={product_name}"

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