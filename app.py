import time

from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from src.panel_layout import PanelLayout


def generate_rods_list(n):
    """Generates a list of n Text objects, each representing a disk of the tower"""
    return [Text(" "*(n-i)+"█"*i, style="green")+Text(f"{i}", style="blue on white")+Text("█"*i+" "*(n-i), style="green") for i in range(n+1)]


def generate_rods_string(rod_list):
    """Takes the list of Text objects and converts it into one object to display the tower"""
    rods_string = Text("")
    for line in rod_list:
        rods_string += line+Text("\n")
    return rods_string


def main():
    layout = PanelLayout.make_layout()
    layout['footer'].update(Panel('footer', title='footer'))
    rods = generate_rods_list(4)
    rods_string = generate_rods_string(rods)
    layout['main'].update(Panel(rods_string, title='main'))
    with Live(layout, refresh_per_second=4, screen=True):
        for i in range(10):
            layout['footer'].update(Panel('footer', title='footer'))
            layout['main'].update(Panel(rods_string, title="main"))
            time.sleep(1)


if __name__ == "__main__":
    main()
