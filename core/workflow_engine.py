# core/workflow_engine.py
import json
from core.web_automation import WebAutomator
from core.email_handler import EmailSender
from core.desktop_auto import DesktopAutomator
from core.database import WorkflowDB

class WorkflowEngine:
    def __init__(self):
        self.modules = {
            "web": WebAutomator(),
            "email": EmailSender(smtp_server="smtp.gmail.com", port=587, email="seu_email@gmail.com", password="senha"),
            "desktop": DesktopAutomator(),
            "database": WorkflowDB()
        }
    
    def run_workflow(self, workflow_file):
        try:
            with open(workflow_file) as f:
                workflow = json.load(f)
            
            print(f"Executando workflow: {workflow['name']}")
            for step in workflow["steps"]:
                module = self.modules[step["module"]]
                action = step["action"]
                params = step.get("params", {})
                
                if step["module"] == "web" and step["action"] == "scrape":
                    step["action"] = "scrape_data"
                
                print(f"  -> Executando {action} no módulo {step['module']}")
                getattr(module, action)(**params)
                
        except Exception as e:
            print(f"Erro no workflow: {e}")
        finally:
            # Garante que recursos são liberados
            if "web" in self.modules:
                self.modules["web"].close()

# Exemplo de uso:
if __name__ == "__main__":
    engine = WorkflowEngine()
    engine.run_workflow("workflows/report.json")