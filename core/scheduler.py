import schedule
import time
from core.workflow_engine import WorkflowEngine
import json
from pathlib import Path
import os
import threading

class Scheduler:
    def __init__(self, config_path="config/workflows.json"):
        self.config_path = Path(__file__).parent.parent / config_path
        self._stop_event = threading.Event()
    
    def _job(self, workflow_file):
        """Executa um workflow específico"""
        engine = WorkflowEngine()
        engine.run_workflow(workflow_file)
    
    def load_config(self):
        """Carrega a configuração do arquivo JSON"""
        try:
            with open(self.config_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"Arquivo não encontrado: {self.config_path}")
        except json.JSONDecodeError:
            raise Exception(f"JSON inválido em: {self.config_path}")
    
    def setup(self):
        """Configura as tarefas agendadas"""
        config = self.load_config()
        for task in config.get("tasks", []):
            schedule.every().day.at(task["time"]).do(
                self._job, 
                task["workflow_file"]
            )
    
    def run(self):
        """Executa o scheduler em background"""
        self.setup()
        while not self._stop_event.is_set():
            schedule.run_pending()
            time.sleep(1)
    
    def stop(self):
        """Para a execução do scheduler"""
        self._stop_event.set()

# Singleton global (opcional)
scheduler = Scheduler()

# Código executável apenas quando rodado diretamente
if __name__ == "__main__":
    scheduler = Scheduler()
    try:
        scheduler.run()
    except KeyboardInterrupt:
        scheduler.stop()

        