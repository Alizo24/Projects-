import flet as ft
import os

def main(page: ft.Page):
    text_editor = ft.TextField(multiline=True, expand=True)
    word_count_label = ft.Text(value="Word Count: 0")

    # Función para guardar 
    def save_file_action(event):
        file_content = text_editor.value
        file_path = os.path.join("WEB2", "saved_file.txt")
        try:
            os.makedirs("WEB2", exist_ok=True)  
            with open(file_path, "w") as file:
                file.write(file_content)
            page.todobien_show("File saved successfully.")
        except Exception as e:
            page.todobien_show(f"Error: {str(e)}")

    # Para seleccionar un archivo
    file_picker = ft.FilePicker()

    def file_opened(e: ft.FilePickerResultEvent):
        if e.files:
            text_content = []
            with open(str(e.files[0].path), "r") as file:
                for line in file.readlines():
                    text_content.append(line)  
                text_editor.value = "\n".join(text_content)  
                update_word_count()
        else:
            page.snackbar_show("No file was selected or operation was cancelled.")

    # Attach the event handler to the FilePicker
    file_picker.on_result = file_opened

    # Add the FilePicker to the page overlay
    page.overlay.append(file_picker)

    # Update word count
    def update_word_count():
        words = len(text_editor.value.split())
        word_count_label.value = f"Word Count: {words}"
        page.update()

    text_editor.on_change = lambda event: update_word_count()

    # New  
    def new_file_action(event):
        text_editor.value = ""
        update_word_count()

    # Open 
    def open_file_action(event):
        file_picker.pick_files(allow_multiple=True)  # Allow multiple files to be picked

    # Button controls
    new_file_btn = ft.ElevatedButton(text="New", on_click=new_file_action)
    open_file_btn = ft.ElevatedButton(text="Open", on_click=open_file_action)
    save_file_btn = ft.ElevatedButton(text="Save", on_click=save_file_action)

    page.add(new_file_btn, open_file_btn, save_file_btn, word_count_label, text_editor)

    ft.app(target=main)
    
    #https://www.geeksforgeeks.org/python-os-makedirs-method/
