"""Seletores (locators) dos elementos usados pelo Selenium."""
from selenium.webdriver.common.by import By


class BaseLocators:
    # Selo "FUN MODE": confirma que o jogo carregou no modo demonstração
    FUN_MODE = (By.CLASS_NAME, "fun-mode")

    # Payout mais recente no histórico de resultados do jogo
    CURR_PAYOUT = (
        By.CSS_SELECTOR,
        "body > app-root > app-game > div > div.main-container "
        "> div.w-100.h-100 > div > div.game-play "
        "> div.result-history.disabled-on-game-focused "
        "> app-stats-widget > div > div.payouts-wrapper > div "
        "> app-payout-item:nth-child(1) > div"
    )


class LVPageLocators(BaseLocators):
    GAME_IFRAME = (By.CSS_SELECTOR, "#game > iframe")


class PUPageLocators(BaseLocators):
    GAME_IFRAME = (By.ID, 'iframe')
