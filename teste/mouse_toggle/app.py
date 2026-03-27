# app.py - Interface grafica

import tkinter as tk
from tkinter import messagebox
import keyboard

from config import load_config, save_config
from mouse_swap import is_swapped, toggle_buttons, restore_normal


class MouseToggleApp:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Mouse Button Toggle")
        self.janela.geometry("280x150")

        self.config = load_config()
        self.invertido = is_swapped()
        self.hotkey_atual = None

        self.criar_interface()
        self.registrar_hotkey(self.config.get("hotkey", "F9"))
        self.atualizar_status()

        self.janela.protocol("WM_DELETE_WINDOW", self.ao_fechar)

    def criar_interface(self):
        self.label_status = tk.Label(self.janela, text="Modo Normal")
        self.label_status.pack(pady=10)

        self.botao_toggle = tk.Button(self.janela, text="Alternar", command=self.alternar)
        self.botao_toggle.pack()

        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Label(frame, text="Hotkey:").pack(side="left")

        self.entry_hotkey = tk.Entry(frame, width=8)
        self.entry_hotkey.pack(side="left", padx=5)
        self.entry_hotkey.insert(0, self.config.get("hotkey", "F9"))

        tk.Button(frame, text="Aplicar", command=self.aplicar_hotkey).pack(side="left")

    def atualizar_status(self):
        if self.invertido:
            self.label_status.config(text="Invertido")
        else:
            self.label_status.config(text="Normal")

    def alternar(self):
        self.invertido = toggle_buttons()
        self.atualizar_status()

    def alternar_por_hotkey(self):
        self.invertido = toggle_buttons()
        self.janela.after(0, self.atualizar_status)

    def registrar_hotkey(self, tecla):
        if self.hotkey_atual:
            try:
                keyboard.remove_hotkey(self.hotkey_atual)
            except:
                pass
        try:
            keyboard.add_hotkey(tecla, self.alternar_por_hotkey)
            self.hotkey_atual = tecla
        except:
            messagebox.showerror("Erro", "Hotkey invalida")

    def aplicar_hotkey(self):
        nova = self.entry_hotkey.get().strip()
        if nova:
            self.registrar_hotkey(nova)
            self.config["hotkey"] = nova
            save_config(self.config)

    def ao_fechar(self):
        restore_normal()
        try:
            keyboard.unhook_all()
        except:
            pass
        self.janela.destroy()

    def rodar(self):
        self.janela.mainloop()
