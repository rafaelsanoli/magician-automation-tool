from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import logging

class WebAutomator:
    def __init__(self):
        self.driver = None
        logging.basicConfig(filename='automation.log', level=logging.INFO)
    
    def _init_driver(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1280,1024")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    def fill_form(self, url, fields):
        try:
            if not self.driver:
                self.driver = self._init_driver()
            
            self.driver.get(url)
            for field in fields:
                element = self.driver.find_element(By.NAME, field['name'])
                element.send_keys(field['value'])
            logging.info(f"Formulário em {url} preenchido com sucesso")
            
        except Exception as e:
            logging.error(f"Erro ao preencher formulário: {str(e)}")
            raise

    def scrape_data(self, url, selectors):
        """Extrai dados de uma página web usando seletores CSS."""
        if not self.driver:
            self.driver = self._init_driver()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        data = {}
        for key, selector in selectors.items():
            element = soup.select_one(selector)
            data[key] = element.text if element else None
        return data

    def open_new_tab(self, url):
        """Abre uma nova aba e navega para a URL."""
        if not self.driver:
            self.driver = self._init_driver()
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)

    def close(self):
        """Fecha o navegador."""
        if self.driver:
            self.driver.quit()
            self.driver = None

# Exemplo de uso:
if __name__ == "__main__":
    automator = WebAutomator()
    automator.fill_form(
        url="https://exemplo.com/formulario",
        fields=[
            {"name": "nome", "value": "João Silva"},
            {"name": "email", "value": "joao@exemplo.com"}
        ]
    )
    automator.close()

    data = automator.scrape_data(
        url="https://exemplo.com/produtos",
        selectors={
            "titulo": "h1.produto-titulo",
            "preco": ".preco"
        }
    )
    print(data)

    automator.open_new_tab("https://google.com")
