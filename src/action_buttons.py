import flet as ft


def generate_json_download_button():
    """
    Generates a button to download the JSON file.

    Returns:
        ft.ElevatedButton: The button to download the JSON file.
    """
    # Button to download the JSON file
    json_download_button = ft.ElevatedButton(
        text="Download JSON file",
        style=ft.ButtonStyle(padding=10),
        on_click=lambda _: print("Download JSON file clicked"),
    )

    return json_download_button


def generate_text_download_button():
    """
    Generates a button to download the text file.

    Returns:
        ft.ElevatedButton: The button to download the text file.
    """
    # Button to download the text file
    text_download_button = ft.ElevatedButton(
        text="Download Text file",
        style=ft.ButtonStyle(padding=10),
        on_click=lambda _: print("Download Text file clicked"),
    )

    return text_download_button


def generate_generation_button():
    """
    Generates a button to generate the output.

    Returns:
        ft.ElevatedButton: The button to generate the output.
    """
    # Button to generate the output
    generation_button = ft.ElevatedButton(
        text="Generate Output",
        style=ft.ButtonStyle(padding=10),
        on_click=lambda _: print("Generate Output clicked"),
    )

    return generation_button
