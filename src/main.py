import flet as ft

from id import generate_id_container
from json_upload import generate_json_container
from action_buttons import (
    generate_json_download_button,
    generate_text_download_button,
    generate_generation_button,
)


def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        if e.ctrl and e.alt and e.key == "M":
            # TODO: Toggle the visibility of the menu
            pass

    page.on_keyboard_event = on_keyboard

    # Configuration section
    configuration_section = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text(
                        "Configuration",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            # ID input and JSON upload
            ft.Row(
                controls=[
                    generate_id_container(),
                    generate_json_container(),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                expand=True,
            ),
            # Actions
            ft.Row(
                controls=[
                    generate_generation_button(),
                    generate_json_download_button(),
                    generate_text_download_button(),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                expand=True,
            ),
        ]
    )

    # Last row: Output

    # Set the title of the page
    page.title = "Scientific Programming - Peer Review"

    page.add(
        configuration_section,
    )


ft.app(main)
