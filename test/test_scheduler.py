from core.compat import load_schedule_config
from core.scheduler import Scheduler
import pytest

def test_scheduler_run(mocker):  # Agora funciona com pytest-mock instalado
    mock_engine = mocker.patch('core.workflow_engine.WorkflowEngine')
    scheduler = Scheduler()
    scheduler.setup()

def test_scheduler_initialization():
    scheduler = Scheduler()
    assert hasattr(scheduler, 'load_config')

def test_config_loading(tmp_path):
    test_config = tmp_path / "test_config.json"
    test_config.write_text('{"tasks": []}')
    
    scheduler = Scheduler(test_config)
    config = scheduler.load_config()
    assert config == {"tasks": []}

    