from flet import *
from flet.types import AnimationValue


class Content(UserControl):

    def __init__(self):
        super().__init__()
        self.like = Text('0', size=14)
        self.dislike = Text('0', size=14)

    def build(self):
        content = Container(
            content=Column([
                Container(
                    content=Text(
                        'Its a coffee',
                        size=20,
                        italic=True,
                        color=colors.WHITE,
                    ),
                    alignment=alignment.center,
                    padding=0,
                    margin=0,
                ),
                Image(
                    src=f'cofe.jpg',
                    border_radius=10
                ),
                Row(
                    controls=[
                        Row(
                            controls=[
                                Container(
                                    content=IconButton(
                                        icons.THUMB_UP,
                                        on_click=self.count_like,
                                    ),
                                ),
                                Container(
                                    content=self.like
                                ),
                                Container(
                                    content=IconButton(
                                        icons.THUMB_DOWN,
                                        on_click=self.count_dislike,
                                    ),
                                ),
                                Container(
                                    content=self.dislike
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        Row(
                            controls=[
                                Container(
                                    content=Text(
                                        f'Price: 500',
                                        size=16,
                                        italic=True,
                                        color=colors.TEAL_ACCENT,
                                        weight=FontWeight.BOLD
                                    ),
                                ),
                            ],
                            alignment=MainAxisAlignment.END,
                        )
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Divider(height=8, thickness=1, color=colors.WHITE10),
                Container(
                    content=Text(
                        'Description: \nsome text and describe or description coffee '
                        '\nsome text and describe or description coffee '
                        '\nsome text and describe or description coffee '
                        '\nsome text and describe or description coffee '
                        '\nsome text and describe or description coffee',
                        size=14,
                        italic=True,
                    )
                ),
                ElevatedButton('Byu', width=100)
            ]),
            bgcolor=colors.PINK_600,
            padding=10,
            border_radius=10,
            alignment=alignment.center,
            expand=True,
        )

        return Container(
            content=Row(
                controls=[content]
            )
        )

    def count_like(self, e):
        self.like.value = str(int(self.like.value) + 1)
        self.update()

    def count_dislike(self, e):
        self.dislike.value = str(int(self.dislike.value) + 1)
        self.update()
