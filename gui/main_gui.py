import tkinter as tk
from tkinter import messagebox
from core.caesar_cipher import CaesarCipher

def load_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    ascii_content = content.encode('latin1', 'replace').decode('latin1')
    return ascii_content

def load_cipher(filename):
    with open(filename, 'r', encoding='latin1') as file:
        content = file.read()
    return content

def toggle_text_input():
    if load_file_var.get():
        text_entry.config(state='disabled')
    else:
        text_entry.config(state='normal')

def execute_action():
    shift = int(shift_entry.get())
    idioma = idioma_entry.get().lower()
    alphanumeric = alphanumeric_var.get()
    incluir_especiales = incluir_especiales_var.get()
    cipher = CaesarCipher(idioma, incluir_especiales, alphanumeric)
    
    if action_var.get() == 'cipher':
        if load_file_var.get():
            text_plain = load_txt('data/plain.txt').strip().lower()
        else:
            text_plain = text_entry.get().strip().lower()
        result = cipher.encrypt(text_plain, shift)
    else:
        if load_file_var.get():
            encrypted_text = load_cipher('data/cipher_text.txt')
        else:
            encrypted_text = text_entry.get().strip().lower()
        result = cipher.decrypt(encrypted_text, shift)
    
    messagebox.showinfo("Resultado", result)

def main_GUI():
    global text_entry, shift_entry, idioma_entry, action_var, load_file_var, alphanumeric_var, incluir_especiales_var

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Cifrado César")

    # Variables
    action_var = tk.StringVar(value='cipher')
    load_file_var = tk.BooleanVar()
    alphanumeric_var = tk.BooleanVar()
    incluir_especiales_var = tk.BooleanVar()

    # Widgets
    tk.Label(root, text="Seleccione una opción:").pack()
    tk.Radiobutton(root, text="Cifrar texto", variable=action_var, value='cipher').pack()
    tk.Radiobutton(root, text="Descifrar texto", variable=action_var, value='decrypt').pack()

    tk.Checkbutton(root, text="Cargar archivo", variable=load_file_var, command=toggle_text_input).pack()

    tk.Label(root, text="Texto:").pack()
    text_entry = tk.Entry(root)
    text_entry.pack()

    tk.Label(root, text="Desplazamiento:").pack()
    shift_entry = tk.Entry(root)
    shift_entry.pack()

    tk.Label(root, text="Idioma (es/en):").pack()
    idioma_entry = tk.Entry(root)
    idioma_entry.pack()

    tk.Checkbutton(root, text="¿Incluir números?", variable=alphanumeric_var).pack()
    tk.Checkbutton(root, text="¿Incluir caracteres especiales?", variable=incluir_especiales_var).pack()

    tk.Button(root, text="Ejecutar", command=execute_action).pack()

    # Iniciar el bucle principal de la interfaz
    root.mainloop()

if __name__ == "__main__":
    main_GUI()