from rich.layout import Layout


class PanelLayout:
    """Define panel layout"""

    @classmethod
    def make_layout(self, initial_screen: bool) -> Layout:
        if not initial_screen:
            layout = Layout(name='root')
            layout.split_column(
                Layout(name='main', ratio=8),
                Layout(name='footer', ratio=2)
            )
        else:
            layout = Layout(name='initial_screen')

        return layout