import asyncio
from playwright.async_api import async_playwright

import subprocess
import os
import time

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://google.com")
        # print(await page.title())
        await page.fill("textarea", "Exemplo Hello World Python")
        await page.press("textarea", 'Enter')
        input("Pressione Enter para sair...")  # Pausa para manter o navegador aberto
        await browser.close()

def close_chrome():
    """Fecha todos os processos do Google Chrome no Windows."""
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

if __name__ == "__main__":
    asyncio.run(main())