# 🧙‍♂️ Magician Automation Tool

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)]()
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![Tests](https://img.shields.io/badge/tests-pytest-passing)]()

> Ferramenta de automação modular com suporte a web, desktop e e-mail. Crie seus próprios workflows com JSON e automatize tarefas rotineiras com poucos cliques!

---

## ✨ Funcionalidades Implementadas

### ✅ Engine de Workflows
- Execução de arquivos `.json` contendo a sequência de ações.
- Encadeamento entre módulos (web → e-mail, etc).

### 🌐 Automação Web
- Navegação em sites com Selenium.
- Suporte a scraping (estrutura pronta).
- Abertura de URLs e preenchimento de formulários.

### 🖥️ Automação Desktop
- Movimentação de mouse e teclado (`pyautogui`).
- Reconhecimento de elementos visuais com OpenCV.
- Suporte básico a gravação de ações.

### ✉️ Manipulação de E-mails
- Envio automático com SMTP.
- Leitura e filtragem com IMAP.

### 💾 Banco de Dados
- Banco SQLite embutido para armazenamento de workflows.
- Suporte a operações CRUD (criar, ler, atualizar, deletar).

### 🗓️ Agendamento de Tarefas
- Execução automática em horários definidos com `schedule`.

---

## 📦 Instalação

### 🔧 Requisitos
- Python 3.9+
- Pip instalado

### 📥 Instale as dependências

```bash
pip install pyautogui schedule pytest
```
Ou use pip install -r requirements.txt se disponível.
---


### 🚀 Como Usar
1. Crie um workflow JSON:
```bash
{
  "name": "Relatório Automático",
  "steps": [
    {"module": "web", "action": "open", "url": "https://site.com"},
    {"module": "email", "action": "send", "to": "gerente@empresa.com"}
  ]
}
```
2. Execute com:
```bash
python main.py --workflow workflow.json
```
O sistema irá interpretar e executar as ações na ordem definida.

---

### 🗂️ Estrutura do Projeto

```bash
magician-automation-tool/
├── core/
│   ├── web_automation.py
│   ├── desktop_auto.py
│   ├── email_handler.py
│   ├── database.py
│   ├── scheduler.py
│   ├── integration.py
│   └── workflow_engine.py
├── main.py
├── setup.py
├── pyproject.toml
```
---

### 🔭 Roadmap Futuro

## 🎯 Curto Prazo

-Interface gráfica (PyQt5)

-Editor de workflows visual (drag-and-drop)

-Dashboard com logs e métricas

## 🌐 Médio Prazo

-APIs externas (Google Sheets, Slack)

-OCR com Tesseract

-Exportação em PDF dos resultados

-Hospedagem via Streamlit/FastAPI

## 🧠 Longo Prazo

-Classificação de e-mails com Machine Learning

-Geração automática de workflows com IA

-Sistema de plugins/extensões

### 🧪 Rodando os Testes

Este projeto utiliza pytest. Execute os testes com:
```bash
pytest
```
---

### 📖 Licença

Distribuído sob a licença MIT. Veja LICENSE para mais detalhes.

---

### 🤝 Contribuindo

Contribuições são muito bem-vindas! Abra uma issue, sugira melhorias ou envie seu pull request.



