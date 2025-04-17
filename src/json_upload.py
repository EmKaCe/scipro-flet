import flet as ft


def submit_json(e: ft.FilePickerResultEvent, json_text: ft.Text) -> None:
    """
    Function to handle the submission of the selected JSON file.
    It updates the selected JSON file text.

    Args:
        e (ft.FilePickerResultEvent): The event containing the selected file information.
        json_text (ft.Text): The text element to update with the selected JSON file name.
    """
    # Update json_text with the selected JSON file name
    if e.files:
        json_text.value = f"Currently selected JSON file: {e.files[0].name}"
    else:
        json_text.value = "Currently selected JSON file: None"

    # Update the text element with the selected JSON file name
    json_text.update()


def generate_json_container():
    """
    Generates a container with a file upload button to upload a JSON file.

    Returns:
        ft.Container: The container with the file upload button and explanation text.
    """
    # Text explanation with the selected JSON file
    json_text = ft.Text(value="Currently selected JSON file: None")

    # File picker for uploading JSON files
    json_file_picker = ft.FilePicker(on_result=lambda e: submit_json(e, json_text))

    # Button to upload the JSON file
    json_upload_button = ft.ElevatedButton(
        text="Upload JSON file",
        style=ft.ButtonStyle(padding=10),
        on_click=lambda _: json_file_picker.pick_files(
            allow_multiple=False, allowed_extensions=["json"]
        ),
    )

    # JSON file upload container with explanation text
    return ft.Card(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="Upload the JSON file with the student data."),
                    json_text,
                    json_upload_button,
                    json_file_picker,
                ]
            ),
            alignment=ft.alignment.center,
            padding=20,
        ),
        height=200,
    )
