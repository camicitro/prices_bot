# Con selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from base_scraper import BaseScraper

class CotoScraper(BaseScraper):
    def scrape(self, product_name):
        base_url = f"https://www.cotodigital.com.ar/sitios/cdigi/categoria?_dyncharset=utf-8&Dy=1&Ntt={product_name}"
        
        # Configuración de Selenium para Chrome
        options = Options()
        #options.add_argument("--headless") 

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)

        driver.get(base_url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.producto-card"))
            )
        except:
            print("Error al cargar la página o no se encontraron productos.")
            driver.quit()
            return []

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
        
        driver.quit()

        return products
