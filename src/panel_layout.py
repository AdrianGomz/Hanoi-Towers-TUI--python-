from rich.layout import Layout


class PanelLayout:
    """Define panel layout"""

    @classmethod
    def make_layout(self) -> Layout:
        layout = Layout(name='root')
        layout.split_column(
            Layout(name='main', ratio=8),
            Layout(name='footer', ratio=2)
        )
        return layout
