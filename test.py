import tkinter as tk
from tkinter import messagebox

def main():
      if alert_confirm("Confirmação", "Deseja confirmar?"):
        print("Operação confirmada")
      else:
        print("Operação cancelada")

def alert_confirm(title: str, message: str) -> bool:
    """Fecha todos os processos do Google Chrome no Windows."""
    print("test")

    root = tk.Tk()
    root.withdraw()

    resposta = messagebox.askyesno(
        title=title,
        message=message
    )

    root.destroy()
    return resposta

if __name__ == "__main__":
    main()