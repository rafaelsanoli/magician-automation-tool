import os
os.environ['DISPLAY'] = ':99'  # Adicione no topo do arquivo
import pyautogui
import time
import keyboard

class DesktopAutomator:
    def click(self, x, y, clicks=1):
        """Clica nas coordenadas (x, y)."""
        pyautogui.click(x, y, clicks=clicks)
    
    def type(self, text, interval=0.1):
        """Digita um texto com intervalo entre teclas."""
        pyautogui.write(text, interval=interval)

    def locate_image(self, image_path, confidence=0.9):
        """Encontra a posição de uma imagem na tela."""
        try:
            pos = pyautogui.locateOnScreen(image_path, confidence=confidence)
            return pos
        except pyautogui.ImageNotFoundException:
            print("Imagem não encontrada.")
            return None

    def record_macro(self, output_file="macro.txt"):
        """Grava ações do teclado/mouse."""
        print("Pressione F10 para começar a gravar e F11 para parar...")
        keyboard.wait("F10")
        print("Gravando... Pressione F11 para parar.")
        actions = []
        while not keyboard.is_pressed("F11"):
            x, y = pyautogui.position()
            actions.append(f"move,{x},{y}")
        with open(output_file, "w") as f:
            f.write("\n".join(actions))
        print(f"Macro salva em {output_file}")

# Exemplo de uso:
if __name__ == "__main__":
    auto = DesktopAutomator()
    time.sleep(3)  # Tempo para posicionar o mouse
    auto.click(100, 200)  # Clica em (x=100, y=200)
    auto.type("Hello, World!")

    button_pos = auto.locate_image("botao_ok.png")
    if button_pos:
        auto.click(button_pos.left, button_pos.top)