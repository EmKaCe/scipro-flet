import flet as ft


def submit_id(selected_id: ft.TextField, selected_id_text: ft.Text) -> None:
    """
    Function to handle the submission of the selected ID.
    It updates the selected ID text and clears the input field.

    Args:
        selected_id (ft.TextField): The text field containing the selected ID.
        selected_id_text (ft.Text): The text element to update with the selected ID.
    """

    # TODO: Refactor this function to use local storage to read and write the selected ID

    # Update selected_id_text with the selected ID, if id is empty set it to None
    if selected_id.value == "":
        selected_id_text.value = "Currently selected student: None"
    else:
        selected_id_text.value = f"Currently selected student: {selected_id.value}"

    # Update the text element with the selected ID
    selected_id_text.update()

    # Clear the input field
    selected_id.value = ""
    selected_id.update()


def generate_id_container() -> ft.Container:
    """
    Function to generate the container for the selected ID input field.
    Returns:
        ft.Container: The container with the selected ID input field and explanation text.
    """

    # Text field for the selected ID
    selected_id_input = ft.TextField(
        label="SciPro_ID",
        hint_text="ID of the student",
        width=500,
        on_submit=lambda _: submit_id(selected_id_input, selected_id_text),
    )

    # Text explanation with the selected ID
    selected_id_text = ft.Text(value="Currently selected student: None")

    # Button to submit the selected ID
    selected_id_button = ft.ElevatedButton(
        text="Submit",
        on_click=lambda _: submit_id(selected_id_input, selected_id_text),
        style=ft.ButtonStyle(padding=10),
    )

    # SciPro_ID input container with explanation text
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        value="Enter the scipro_id of the student you want to review."
                    ),
                    selected_id_input,
                    selected_id_text,
                    selected_id_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=20,
            alignment=ft.alignment.center,
        ),
        height=200,
    )
