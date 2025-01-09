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

class CarrefourScraper(BaseScraper):
    def scrape(self, product_name):
        base_url = f"https://www.carrefour.com.ar/{product_name}?_q={product_name}&map=ft"
        
        # Configuración de Selenium para Chrome
        options = Options()
        #options.add_argument("--headless") 

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

        import time
        time.sleep(3) 
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []

        # Selección de productos
        product_items = soup.select("section.vtex-product-summary-2-x-container")
        for item in product_items:
            try:
                name = item.select_one(".vtex-product-summary-2-x-productNameContainer span").text.strip()

                price_container = item.select_one(".valtech-carrefourar-product-price-0-x-currencyContainer")
                if price_container:
                    code_part = price_container.select_one(".valtech-carrefourar-product-price-0-x-currencyCode")
                    integer_parts = price_container.select(".valtech-carrefourar-product-price-0-x-currencyInteger")
                    group_parts = price_container.select(".valtech-carrefourar-product-price-0-x-currencyGroup")
                    fraction_part = price_container.select_one(".valtech-carrefourar-product-price-0-x-currencyFraction")

                    integer_with_groups = ""
                    for i, integer in enumerate(integer_parts):
                        integer_with_groups += integer.text  
                        if i < len(group_parts):  
                            integer_with_groups += group_parts[i].text

                    price = f"{code_part.text}{integer_with_groups},{fraction_part.text if fraction_part else '00'}".strip()
                else:
                    price = "No disponible"

                image_url = item.select_one("img.vtex-product-summary-2-x-imageNormal")["src"]

                product_url = "https://www.carrefour.com.ar" + item.select_one("a.vtex-product-summary-2-x-clearLink")["href"]

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
