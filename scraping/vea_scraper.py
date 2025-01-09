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

class VeaScraper(BaseScraper):
    def scrape(self, product_name):
        base_url = f"https://www.vea.com.ar/{product_name}?_q={product_name}&map=ft"
        
        # Configuración de Selenium para Chrome
        options = Options()
        options.add_argument("--headless") 

        service = Service(ChromeDriverManager().install())
        
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get(base_url)
        
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "section.vtex-product-summary-2-x-container"))
            )
        except:
            print("Error al cargar la página o no se encontraron productos.")
            driver.quit()
            return []

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []

        # Selección de productos
        product_items = soup.select("section.vtex-product-summary-2-x-container")
        for item in product_items:
            try:
                name = item.select_one(".vtex-product-summary-2-x-nameWrapper").text.strip()
                
                price_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".veaargentina-store-theme-1dCOMij_MzTzZOCohX1K7w")))
                price = price_element.text.strip() if price_element.text else "Precio no disponible"

                image_url = item.select_one(".vtex-product-summary-2-x-image")["src"]
                
                product_url = "https://www.vea.com.ar" + item.select_one(".vtex-product-summary-2-x-clearLink")["href"]

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
