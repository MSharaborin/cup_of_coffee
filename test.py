from flet import *

def main(page: Page):

    page.title = "NavigationBar Example"
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.EXPLORE, label="Explore"),
            NavigationDestination(icon=icons.COMMUTE, label="Commute"),
            NavigationDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon=icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    page.add(Text("Body!"))

app(target=main)
