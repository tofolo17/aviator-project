"""Coleta de payouts do Aviator via Selenium.

O Betwarrior parece travar o jogo na entrada de um robô.
Analisar sem login em: https://lvbet.com/br/slots/aviator/.

Incrível descoberta... As odds são compartilhadas entre os sites.
"""
from pathlib import Path

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.game_pages import GamePageLV

# Caminho absoluto do arquivo de saída, independente de onde o pytest roda
PAYOUTS_FILE = Path(__file__).resolve().parent.parent / 'data' / 'payouts.txt'


def _new_driver():
    # Instância do driver (o webdriver-manager baixa o ChromeDriver)
    driver = Chrome(service=Service(ChromeDriverManager().install()))

    # Maximiza browser
    driver.maximize_window()

    # Aguarde implícito
    driver.implicitly_wait(30)
    return driver


@pytest.fixture
def browser_00():
    driver = _new_driver()
    yield driver
    driver.quit()


@pytest.fixture
def browser_01():
    # Segundo navegador, reservado para coletar de dois sites em paralelo
    driver = _new_driver()
    yield driver
    driver.quit()


def test_lv(browser_00):
    """Coletor contínuo: roda até ser interrompido (Ctrl+C)."""
    # Instancia a página do jogo e a carrega
    lv_page = GamePageLV(browser_00)
    lv_page.load()

    # Entra no iFrame do jogo e checa se a ação foi bem sucedida
    lv_page.enter_game()
    assert lv_page.check_success()

    # Último payout
    lp_lv = ""

    while True:
        payout_lv = lv_page.get_current_payout()
        assert '.' in payout_lv

        # Se o último payout é diferente do atual, escreva
        if lp_lv != payout_lv:
            lp_lv = payout_lv

            with open(PAYOUTS_FILE, 'a') as f:
                f.write(f'{str(payout_lv)}\n')


def test_lv_2(browser_00):
    # Rascunho: apenas abre a página (experimento não concluído)
    lv_page = GamePageLV(browser_00)
    lv_page.load()
