# ui/editor.py
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, 
                             QPushButton, QFileDialog, QMessageBox)
import json

class EditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Workflow")
        self.setGeometry(200, 200, 600, 400)
        
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText('''{
  "name": "Meu Workflow",
  "steps": [
    {
      "module": "web",
      "action": "scrape",
      "params": {"url": "https://exemplo.com"}
    }
  ]
}''')
        
        self.btn_save = QPushButton("Salvar Workflow")
        
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.btn_save)
        self.setLayout(layout)
        
        self.btn_save.clicked.connect(self.save_workflow)
    
    def save_workflow(self):
        try:
            workflow_data = json.loads(self.text_edit.toPlainText())
            if not self.validate_workflow(workflow_data):
                raise ValueError("Workflow inválido. Certifique-se de que todos os campos obrigatórios estão preenchidos.")

            file_name, _ = QFileDialog.getSaveFileName(
                self, "Salvar Workflow", "workflows", "JSON Files (*.json)")

            if file_name:
                with open(file_name, "w") as f:
                    json.dump(workflow_data, f, indent=4)
                QMessageBox.information(self, "Sucesso", "Workflow salvo com sucesso!")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Erro", "O conteúdo do workflow não é um JSON válido.")
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))

    def validate_workflow(self, workflow):
        """Valida o formato do workflow."""
        required_keys = {"name", "steps"}
        if not isinstance(workflow, dict):
            return False
        if not required_keys.issubset(workflow.keys()):
            return False
        if not isinstance(workflow["steps"], list) or not workflow["steps"]:
            return False
        for step in workflow["steps"]:
            if not all(key in step for key in ("module", "action", "target")):
                return False
        return True

class WorkflowEditor:
    def __init__(self):
        self.workflow = {
            "name": "",
            "steps": []
        }

    def add_step(self, module, action, target):
        """Add a step to the workflow."""
        self.workflow["steps"].append({
            "module": module,
            "action": action,
            "target": target
        })

    def set_name(self, name):
        """Set the name of the workflow."""
        self.workflow["name"] = name

    def save_to_file(self, file_path):
        """Save the workflow to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump(self.workflow, file, indent=4)

# Example usage
if __name__ == "__main__":
    editor = WorkflowEditor()
    editor.set_name("Envio de Relatório")
    editor.add_step("web", "scrape", "https://exemplo.com/dados")
    editor.add_step("email", "send", "gerente@empresa.com")
    editor.save_to_file("../workflows/report.json")