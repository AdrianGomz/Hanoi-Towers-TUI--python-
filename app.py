import time

from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns

from src.panel_layout import PanelLayout
from src.hanoi_towers import generate_moves_list


def generate_rods_disks_list(n, disks_list):
    """Generates a list of n Text objects, each representing a disk of the tower"""
    disks_strings = []
    for i in range(n+1):
        try:
            length = disks_list[i]
            disks_strings.append(Text(" "*(n-length)+"█"*length, style="green")+Text(" ",
                                                                                     style="blue on white")+Text("█"*length+" "*(n-length), style="green"))
        except:
            disks_strings.append(
                Text(" "*(n))+Text(" ", style="blue on white")+Text(" "*(n)))

    return disks_strings[::-1]


def generate_rods_string(n, disk_list):
    """Takes the list of Text objects and converts it into one object to display the tower"""
    rod_list = generate_rods_disks_list(n, disk_list)
    rods_string = Text("")
    for line in rod_list:
        rods_string += line+Text("\n")
    return rods_string


def main():
    layout = PanelLayout.make_layout()
    layout['footer'].update(Panel('footer', title='footer'))

    moves_list = generate_moves_list(4)
    rod_1 = generate_rods_string(4, moves_list[0][0])
    rod_2 = generate_rods_string(4, moves_list[0][1])
    rod_3 = generate_rods_string(4, moves_list[0][2])
    layout['main'].update(
        Panel(Columns([rod_1, rod_2, rod_3]), title="main"))
    with Live(layout, refresh_per_second=4, screen=True):
        for move in moves_list:
            rod_1 = generate_rods_string(4, move[0])
            rod_2 = generate_rods_string(4, move[1])
            rod_3 = generate_rods_string(4, move[2])
            layout['footer'].update(Panel('footer', title='footer'))
            layout['main'].update(
                Panel(Columns([rod_1, rod_2, rod_3]), title="main"))
            time.sleep(1)


if __name__ == "__main__":
    main()
