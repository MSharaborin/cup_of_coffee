from flet import *


class Header(UserControl):

    def build(self):
        return Container(
            content=Text(
                'Cup of Coffee',
                size=34,
                color=colors.PINK_600,
                italic=True,
                weight=FontWeight.BOLD
            ),
            padding=10,
            alignment=alignment.center,
            border_radius=10,
            expand=True
        )
