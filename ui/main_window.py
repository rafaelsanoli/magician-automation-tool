# ui/main_window.py
from PyQt5.QtWidgets import (QMainWindow, QListWidget, QPushButton, 
                             QVBoxLayout, QWidget, QMessageBox, QTextEdit)
import os
from ui.editor import EditorWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automatizador de Workflows")
        self.setGeometry(100, 100, 800, 600)
        
        # Widgets
        self.list_workflows = QListWidget()
        self.load_workflows()
        
        self.btn_add = QPushButton("Novo Workflow")
        self.btn_run = QPushButton("Executar Selecionado")
        self.btn_open_editor = QPushButton("Abrir Editor de Workflow")
        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.list_workflows)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_run)
        layout.addWidget(self.btn_open_editor)
        layout.addWidget(self.log_view)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Conexões
        self.btn_add.clicked.connect(self.open_editor)
        self.btn_run.clicked.connect(self.run_selected)
        self.btn_open_editor.clicked.connect(self.open_editor)
    
    def load_workflows(self):
        """Carrega workflows da pasta workflows/"""
        self.list_workflows.clear()
        if not os.path.exists("workflows"):
            os.mkdir("workflows")
        
        for file in os.listdir("workflows"):
            if file.endswith(".json"):
                self.list_workflows.addItem(file)
    
    def open_editor(self):
        self.editor = EditorWindow()
        self.editor.show()
    
    def append_log(self, message):
        """Append a log message to the log view."""
        self.log_view.append(message)
    
    def run_selected(self):
        selected = self.list_workflows.currentItem()
        if selected:
            from core.workflow_engine import WorkflowEngine
            engine = WorkflowEngine()
            try:
                engine.run_workflow(f"workflows/{selected.text()}")
                self.append_log(f"Workflow '{selected.text()}' executado com sucesso.")
            except Exception as e:
                self.append_log(f"Erro ao executar workflow '{selected.text()}': {str(e)}")

# Example usage
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())