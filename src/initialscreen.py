from rich.panel import Panel
from rich.text import Text
from pynput.keyboard import Key, Listener


class InitialScreen:
    def __init__(self) -> None:
        self.in_initial_screen = True

    def on_press(self, key):
        try:
            if key.char == 's':
                self.in_initial_screen = False
        except:
            return False

    def on_release(self, key):
        return False

    def key_input(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def display_initial_screen(self):
        with open("start_screen.txt", "r") as file:
            start_panel = Panel(Text(''.join(file.readlines())))
        return start_panel
