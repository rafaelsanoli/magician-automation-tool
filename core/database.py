# core/database.py
import sqlite3

class WorkflowDB:
    def __init__(self, db_path="config/workflows.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS workflows (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            steps TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def save_workflow(self, name, steps):
        """Salva um novo workflow."""
        self.cursor.execute(
            "INSERT INTO workflows (name, steps) VALUES (?, ?)",
            (name, str(steps))
        )
        self.conn.commit()
    
    def get_workflow(self, name):
        """Carrega um workflow pelo nome."""
        self.cursor.execute(
            "SELECT steps FROM workflows WHERE name = ?",
            (name,))
        return self.cursor.fetchone()
    
    def delete_workflow(self, name):
        """Remove um workflow."""
        self.cursor.execute(
            "DELETE FROM workflows WHERE name = ?",
            (name,))
        self.conn.commit()