from flet import *
from header import Header
from content import Content


def main(page: Page):
    page.title = "Cup of Coffee"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.COFFEE),
            NavigationDestination(icon=icons.SEARCH, ),
            NavigationDestination(icon=icons.SHOPPING_CART),
        ]
    )
    page.update()

    # add application's root control to the page
    page.add(Header(), Content())


flet.app(target=main, assets_dir='icons', port=8080)
