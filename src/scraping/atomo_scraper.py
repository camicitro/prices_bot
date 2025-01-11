from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys
import os
import time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from base_scraper import BaseScraper


class AtomoScraper(BaseScraper):
    def scrape(self, product_name):
        base_url = f"https://atomoconviene.com/atomo-ecommerce/module/ambjolisearch/jolisearch?s={product_name}"

        def scraping_logic(driver):
            driver.get(base_url)

            if not self.wait_for_element(driver, By.CSS_SELECTOR, "article.product-miniature"):
                print("No se encontraron productos en la página.")
                return []
            time.sleep(3)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            products = []

            # Selección de productos
            product_items = soup.select("article.product-miniature")
            for item in product_items:
                try:
                    name = item.select_one("p.product-title a").text.strip()

                    price_element = item.select_one(".price").text.strip()
                    if price_element:
                        raw_price = price_element
                        price = raw_price.replace("\xa0", "")  
                    else:
                        price = "Precio no disponible"

                    image_url = item.select_one("a.thumbnail img").get("data-src")

                    product_url = item.select_one("p.product-title a").get("href")

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