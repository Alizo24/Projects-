import flet as ft
import pyperclip

# Morse code dictionary
morse_code_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----", " ": "/"
}

reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}

def reverse_text(text):
    return text[::-1]

def alphabetic_substitution(text, encrypt=True):
    shift = 3 if encrypt else -3  # +3 para encriptar, -3 para desencriptar
    shifted_text = ""
    for char in text:
        if char.isalpha():  # Solo se cambian las letras
            if char.islower():
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            shifted_char = char  # Los caracteres no alfabeticos se mantienen iguales
        shifted_text += shifted_char
    return shifted_text

def decrypt_morse_code(code):
    morse_chars = code.split(' ')
    decoded_message = ""
    for morse_char in morse_chars:
        if morse_char == "/":
            decoded_message += ' '
        else:
            decoded_message += reverse_morse_code_dict.get(morse_char, '')
    return decoded_message

def translate_message(message, option, encrypt=True):
    translated_message = ""
    if option == "Morse Code":
        if encrypt:
            translated_message = " ".join(morse_code_dict.get(char.upper(), "") for char in message)
        else:
            translated_message = decrypt_morse_code(message)
    elif option == "Reverse":
        translated_message = reverse_text(message)
    elif option == "Alphabetic Substitution":
        translated_message = alphabetic_substitution(message, encrypt)
    return translated_message

def handle_input_errors(text, option, encrypt):
    if not text:
        return "Error: Please enter some text to translate."
    if option == "Morse Code" and not encrypt and not all(char in ".-/ " for char in text):
        return "Error: Invalid Morse Code."
    return ""

def textbox_changed(e):
    error_message = handle_input_errors(tb.value, dd.value, encrypt_switch.value)
    if error_message:
        copy_label.value = error_message
        translated_text_field.value = ""
    else:
        translated_message = translate_message(tb.value, dd.value, encrypt_switch.value)
        translated_text_field.value = translated_message
        copy_label.value = ""
    translated_text_field.update()
    copy_label.update()

def copy_to_clipboard(e):
    if translated_text_field.value:
        pyperclip.copy(translated_text_field.value)
        copy_label.value = "Copied to clipboard."
    else:
        copy_label.value = "Nothing to copy."
    copy_label.update()

def main(page: ft.Page):
    global tb, dd, copy_button, copy_label, translated_text_field, encrypt_switch
    tb = ft.TextField(label="Enter text to translate:", on_change=textbox_changed)
    page.add(tb)
    dd = ft.Dropdown(label="Choose translation option:", options=[
        ft.dropdown.Option("Morse Code"),
        ft.dropdown.Option("Reverse"),
        ft.dropdown.Option("Alphabetic Substitution"),
    ], on_change=textbox_changed)
    page.add(dd)
    translated_text_field = ft.TextField(label="Translated Message", disabled=True)
    page.add(translated_text_field)
    encrypt_switch = ft.Switch(label="Encrypt", value=True, on_change=textbox_changed)
    page.add(encrypt_switch)
    copy_button = ft.TextButton(text="Copy to Clipboard", on_click=copy_to_clipboard)
    page.add(copy_button)
    copy_label = ft.Text(value="")
    page.add(copy_label)

if __name__ == "__main__":
    ft.app(target=main)
    

#Desincriptar solo funciona con morse code porque en teoria no se puede desencriptar reverse
# El problema con alphabetic substitution es que cualquier palabra puede estar escrita en un orden diferente y el progrma tendria que tener especificaciones muy precisas para saber si es una palabra escrita normal o encriptada.
#igual si queremos encritar una palabra, por ejemplo hola, nos saldra de forma encriptada(krod), y si escribimos esta traduccion y luego desactivamos la opcion de encriptar(para desencriptar) el codigo nos mostrara hola. 
    #FUENTES:
#https://pythonalgos.com/python-affine-cipher-substitution-cipher/
#https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
# https://www.w3schools.com/python/ref_dictionary_get.asp
#https://www.w3schools.com/python/python_dictionaries.asp
#https://pieriantraining.com/reversing-keys-and-values-in-a-python-dictionary/#:~:text=Method%201%3A%20Using%20a%20For%20Loop&text=Create%20an%20empty%20dictionary%20that,the%20reversed%20key%2Dvalue%20pairs.&text=2.,dictionary%20created%20in%20step%201.
#chatgpt(para las letras de morse code)
#mi tio para la logistica de alphabetic substitution
#sorry por la tardanza, fueron dos semanas de lagrimas y sufrimiento;)
