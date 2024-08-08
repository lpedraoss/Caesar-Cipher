import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
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

    # Cargar la imagen de fondo
    background_image = PhotoImage(file="assets/background.png")

    # Crear un Canvas y colocar la imagen de fondo
    canvas = tk.Canvas(root, width=background_image.width(), height=background_image.height())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    # Variables
    action_var = tk.StringVar(value='cipher')
    load_file_var = tk.BooleanVar()
    alphanumeric_var = tk.BooleanVar()
    incluir_especiales_var = tk.BooleanVar()

    # Estilo oscuro
    dark_bg = "#2e2e2e"
    dark_fg = "#ffffff"
    entry_bg = "#3e3e3e"
    entry_fg = "#ffffff"

    # Widgets
    canvas.create_rectangle(50, 10, 250, 90, fill=dark_bg, outline=dark_bg)
    canvas.create_text(150, 20, text="Seleccione una opción:", fill=dark_fg)
    canvas.create_window(150, 50, window=tk.Radiobutton(root, text="Cifrar texto", variable=action_var, value='cipher', bg=dark_bg, fg=dark_fg, selectcolor=dark_bg))
    canvas.create_window(150, 80, window=tk.Radiobutton(root, text="Descifrar texto", variable=action_var, value='decrypt', bg=dark_bg, fg=dark_fg, selectcolor=dark_bg))

    canvas.create_rectangle(50, 100, 250, 130, fill=dark_bg, outline=dark_bg)
    canvas.create_window(150, 110, window=tk.Checkbutton(root, text="Cargar archivo", variable=load_file_var, command=toggle_text_input, bg=dark_bg, fg=dark_fg, selectcolor=dark_bg))

    canvas.create_rectangle(50, 130, 250, 170, fill=dark_bg, outline=dark_bg)
    canvas.create_text(150, 140, text="Texto:", fill=dark_fg)
    text_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
    canvas.create_window(150, 160, window=text_entry)

    canvas.create_rectangle(50, 180, 250, 220, fill=dark_bg, outline=dark_bg)
    canvas.create_text(150, 190, text="Desplazamiento:", fill=dark_fg)
    shift_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
    canvas.create_window(150, 210, window=shift_entry)

    canvas.create_rectangle(50, 230, 250, 270, fill=dark_bg, outline=dark_bg)
    canvas.create_text(150, 240, text="Idioma (es/en):", fill=dark_fg)
    idioma_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
    canvas.create_window(150, 260, window=idioma_entry)

    canvas.create_rectangle(50, 280, 250, 340, fill=dark_bg, outline=dark_bg)
    canvas.create_window(150, 290, window=tk.Checkbutton(root, text="¿Incluir números?", variable=alphanumeric_var, bg=dark_bg, fg=dark_fg, selectcolor=dark_bg))
    canvas.create_window(150, 320, window=tk.Checkbutton(root, text="¿Incluir caracteres especiales?", variable=incluir_especiales_var, bg=dark_bg, fg=dark_fg, selectcolor=dark_bg))

    #canvas.create_rectangle(50, 350, 250, 380, fill=dark_bg, outline=dark_bg)
    canvas.create_window(150, 350, window=tk.Button(root, text="Ejecutar", command=execute_action, bg=dark_bg, fg=dark_fg))

    # Iniciar el bucle principal de la interfaz
    root.mainloop()

if __name__ == "__main__":
    main_GUI()