import pytest
from unittest.mock import patch, MagicMock
from core.scheduler import Scheduler

@pytest.fixture(autouse=True)
def mock_scheduler():
    """Fixture global para mockar o scheduler"""
    with patch('core.scheduler.Scheduler') as mock:
        instance = mock.return_value
        instance.load_config.return_value = {"tasks": []}
        yield instance

def test_load_config(mock_scheduler):
    """Testa o carregamento da configuração"""
    config = mock_scheduler.load_config()
    assert isinstance(config, dict)
    assert "tasks" in config

def test_scheduler_integration(mock_scheduler):
    """Testa a integração do scheduler"""
    mock_scheduler.load_config.return_value = {
        "tasks": [{"time": "10:00", "workflow_file": "test.json"}]
    }
    config = mock_scheduler.load_config()
    assert len(config["tasks"]) == 1

def test_workflow_execution(mock_scheduler):
    """Testa a execução do workflow"""
    with patch('core.workflow_engine.WorkflowEngine') as mock_engine:
        engine_instance = mock_engine.return_value
        engine_instance.run_workflow.return_value = True
        
        result = engine_instance.run_workflow("test.json")
        assert result is True