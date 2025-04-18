import pytest
import os
from unittest.mock import MagicMock, patch
from core.compat import load_schedule_config

@pytest.fixture(autouse=True)
def mock_environment():
    """Fixture global para todos os testes"""
    # Configura o display virtual
    os.environ['DISPLAY'] = ':99'
    
    # Mocks para todas as dependências externas
    with patch.dict('sys.modules', {
        'pyautogui': MagicMock(),
        'mouseinfo': MagicMock(),
        'Xlib': MagicMock(),
    }):
        yield