# mouse_swap.py - Troca os botoes do mouse usando a API do Windows

import ctypes

user32 = ctypes.WinDLL("user32")

# Constante pra verificar se os botoes estao trocados
SM_SWAPBUTTON = 23


def is_swapped():
    """Verifica se os botoes do mouse estao invertidos."""
    return bool(user32.GetSystemMetrics(SM_SWAPBUTTON))


def swap_buttons(swap):
    """Troca ou restaura os botoes do mouse.
    swap=True inverte, swap=False restaura."""
    user32.SwapMouseButton(swap)


def toggle_buttons():
    """Alterna o estado dos botoes. Retorna True se ficou invertido."""
    novo_estado = not is_swapped()
    swap_buttons(novo_estado)
    return novo_estado


def restore_normal():
    """Restaura os botoes pro modo normal."""
    swap_buttons(False)
