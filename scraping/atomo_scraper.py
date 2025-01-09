#Sin selenium
import requests
from bs4 import BeautifulSoup

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from base_scraper import BaseScraper

class AtomoScraper(BaseScraper):
    def scrape(self, product_name):
        base_url = f"https://atomoconviene.com/atomo-ecommerce/module/ambjolisearch/jolisearch?s={product_name}"
        response = requests.get(base_url)
        
        if response.status_code != 200:
            print(f"Error al acceder al sitio: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        products = []

        # Selección de productos
        product_items = soup.select("article.product-miniature") 
        for item in product_items:
            try:
                name = item.select_one("p.product-title a").text.strip()

                price = item.select_one("div.product-price-and-shipping .price").text.strip()

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
