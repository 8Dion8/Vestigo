from nicegui import Tailwind, ui
import os

COLOR_BG0 = os.environ["COLOR_BG0"]
COLOR_BG1 = os.environ["COLOR_BG1"]
COLOR_GREEN = os.environ["COLOR_GREEN"]
COLOR_RED = os.environ["COLOR_RED"]
COLOR_BLUE = os.environ["COLOR_BLUE"]
COLOR_FG = os.environ["COLOR_FG"]

dark = ui.dark_mode().enable()
ui.query('body').style(f"background-color: {COLOR_BG0}; color: {COLOR_FG}")

with ui.column() as main_col:
    with ui.row() as header_row:
        ui.label('Vestigo').style(f"color: {COLOR_GREEN}").classes("place-self-center").tailwind.font_size("6xl")
        header_row.tailwind.margin("m-10")
    main_col.style(f"background-color: {COLOR_BG1}").classes("place-self-center w-[80vw]")

ui.run()