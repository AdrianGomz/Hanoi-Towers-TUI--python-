import time

from rich.live import Live
from rich.panel import Panel

from src.panel_layout import PanelLayout


def main():
    layout = PanelLayout.make_layout()
    layout['footer'].update(Panel('footer', title='footer'))
    layout['main'].update(Panel('main', title='main'))
    with Live(layout, refresh_per_second=4, screen=True):
        for i in range(10):
            layout['footer'].update(Panel('footer', title='footer'))
            layout['main'].update(Panel('main', title='main'))
            time.sleep(1)


if __name__ == "__main__":
    main()
