import asyncio
from playwright.async_api import async_playwright

import tkinter as tk
from tkinter import messagebox

import subprocess
import os
import time

async def main():
    async with async_playwright() as p:
        confirm_close_chrome = alert_confirm("".join([
            "Deseja permitir que a aplicação assuma o controle do seu navegador Chrome? \n\n",
            "Isso irá fechar todos os processos do Chrome no Windows para abri-los novamente",
        ]))

        if confirm_close_chrome:
            print("sim")
            switch_to_chrome_remote_debugging()

        # browser = await p.chromium.launch(headless=False)
        # page = await browser.new_page()
        # await page.goto("https://google.com")
        # # print(await page.title())
        # await page.fill("textarea", "Exemplo Hello World Python")
        # await page.press("textarea", 'Enter')
        # input("Pressione Enter para sair...")  # Pausa para manter o navegador aberto
        # await browser.close()

def alert_confirm(message: str) -> bool:
    """Fecha todos os processos do Google Chrome no Windows."""
    print("test")

    root = tk.Tk()
    root.withdraw()

    resposta = messagebox.askyesno(
        title="Confirmação",
        message=message
    )

    root.destroy()
    return resposta

def switch_to_chrome_remote_debugging():
    """Fecha todos os processos do Google Chrome no Windows."""
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if not os.path.exists(chrome_path):
        print(f"Erro: O executável do Chrome não foi encontrado em '{chrome_path}'.")
        print("Por favor, ajuste o caminho se for diferente no seu sistema.")
        return None

    try:
        # /IM chrome.exe: Especifica a imagem do processo (o nome do executável)
        # /F: Força o encerramento do processo
        # /T: Encerra o processo e todos os seus processos filhos
        subprocess.run(['taskkill', '/IM', 'chrome.exe', '/F', '/T'], check=True, capture_output=True)
        print("Todos os processos do Chrome foram encerrados.")
    except subprocess.CalledProcessError as e:
        # Erro 128 ocorre se o processo não for encontrado (já estava fechado)
        if "128" in str(e.stderr): # Ou checar se 'No tasks are running' está no stderr
            print("Nenhum processo do Chrome estava rodando para ser encerrado.")
        else:
            print(f"Erro ao encerrar o Chrome: {e.stderr.decode()}")
    except FileNotFoundError:
        print("Comando 'taskkill' não encontrado. Verifique se está em um ambiente Windows.")

    command = [
        chrome_path,
        f"--remote-debugging-port=9222",
        # "--user-data-dir=C:\\temp\\chrome_user_data",
        # Para que o Chrome não se abra em uma aba em branco por padrão e use a sessão do seu perfil principal,
        # você geralmente não coloca o --user-data-dir
        # No entanto, se você quer um ambiente LIMPO, use --user-data-dir para um perfil separado.
    ]

    try:
        # Popen permite que o script Python continue rodando enquanto o Chrome é iniciado
        process = subprocess.Popen(command, shell=False)
        print(f"Chrome iniciado em modo de depuração remota na porta {port}.")
        return process # Retorna o objeto processo caso precise controlá-lo depois
    except Exception as e:
        print(f"Erro ao tentar abrir o Chrome: {e}")
        return None

if __name__ == "__main__":
    asyncio.run(main())