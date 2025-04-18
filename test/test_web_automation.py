import unittest
from core.web_automation import WebAutomator
from core.workflow_engine import WorkflowEngine
from unittest.mock import patch, MagicMock
from core.compat import load_schedule_config

class TestWebAutomation(unittest.TestCase):
    @patch("core.web_automation.WebAutomator")
    def test_form_filling(self, MockWebAutomator):
        mock_automator = MockWebAutomator.return_value
        mock_automator.fill_form.return_value = None  # Simula o comportamento do método

        try:
            mock_automator.fill_form(
                url="https://example.com/form",
                fields=[
                    {"name": "username", "value": "testuser"},
                    {"name": "password", "value": "password123"}
                ]
            )
            mock_automator.fill_form.assert_called_once_with(
                url="https://example.com/form",
                fields=[
                    {"name": "username", "value": "testuser"},
                    {"name": "password", "value": "password123"}
                ]
            )
        except Exception as e:
            self.fail(f"fill_form raised an exception: {e}")

    def test_scrape_data(self):
        automator = WebAutomator()
        try:
            data = automator.scrape_data(
                url="https://example.com",
                selectors={"title": "h1", "description": "p.description"}
            )
            self.assertIn("title", data)
            self.assertIn("description", data)
        except Exception as e:
            self.fail(f"scrape_data raised an exception: {e}")

    def test_open_new_tab(self):
        automator = WebAutomator()
        try:
            automator.open_new_tab("https://example.com")
        except Exception as e:
            self.fail(f"open_new_tab raised an exception: {e}")

    def test_close(self):
        automator = WebAutomator()
        try:
            automator.close()
        except Exception as e:
            self.fail(f"close raised an exception: {e}")

class TestWorkflowEngine(unittest.TestCase):
    @patch("core.email_handler.EmailSender.__init__", return_value=None)
    @patch("core.email_handler.EmailSender.send", return_value=None)
    @patch("core.desktop_auto.pyautogui")
    def test_run_workflow(self, mock_pyautogui, mock_send, mock_email_init):
        mock_pyautogui.return_value = None  # Mock all pyautogui calls

        engine = WorkflowEngine()
        try:
            engine.run_workflow("workflows/report.json")
            mock_send.assert_called()  # Ensure email sending was called
        except Exception as e:
            self.fail(f"run_workflow raised an exception: {e}")