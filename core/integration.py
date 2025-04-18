
from web_automation import WebAutomator
from email_handler import EmailSender
import json

def scrape_and_email(url, selectors, email_config):
    # 1. Scraping
    web = WebAutomator()
    data = web.scrape_data(url, selectors)
    web.close()
    
    # 2. Formata os dados
    body = f"Dados extraídos:\n{json.dumps(data, indent=2)}"
    
    # 3. Envia e-mail
    sender = EmailSender(**email_config)
    sender.send(
        to="destino@exemplo.com",
        subject="Relatório Automatizado",
        body=body
    )

# Uso:
scrape_and_email(
    url="https://exemplo.com/produtos",
    selectors={"titulo": "h1", "preco": ".price"},
    email_config={
        "smtp_server": "smtp.gmail.com",
        "port": 587,
        "email": "seu_email@gmail.com",
        "password": "senha"
    }
)