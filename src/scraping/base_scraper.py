from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from abc import abstractmethod

class BaseScraper:
    def _initialize_driver(self):
        options = Options()
        options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def with_driver(self, func):
        driver = None
        try:
            driver = self._initialize_driver()
            return func(driver)
        finally:
            if driver:
                driver.quit()

    def wait_for_element(self, driver, by, value, timeout=10):
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            print(f"Error esperando elemento: {e}")
            return None
    
    @abstractmethod
    def scrape(self, product_name):

      pass
