# Mouse Button Toggle

Aplicativo simples para Windows que troca os botoes esquerdo e direito do mouse usando uma hotkey.

Util quando o botao esquerdo do mouse esta com defeito.

## Como usar

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Rodar

```bash
python main.py
```

### Na interface

- Clique em **Alternar Modo** pra trocar os botoes
- Configure a **hotkey** que voce quiser (padrao: F9)
- Pressione a hotkey a qualquer momento pra alternar

### Modos

- **Modo Normal** - botoes do mouse no padrao
- **Modo Invertido** - esquerdo vira direito e vice-versa

## Tecnologias

- **Tkinter** - interface grafica
- **keyboard** - hotkeys globais
- **ctypes** - API do Windows pra trocar os botoes

## Licenca

MIT
