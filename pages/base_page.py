"""Page Object base: ações comuns às páginas do jogo."""


class BasePage:
    URL = ''
    LOCATOR = None  # classe de locators definida em cada página filha

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def find(self, by_locator):
        return self.browser.find_element(*by_locator)

    def get_text(self, by_locator):
        el = self.find(by_locator)
        return el.text

    def frame(self, by_locator):
        frame = self.find(by_locator)
        self.browser.switch_to.frame(frame)

    def enter_game(self):
        # O jogo roda dentro de um iframe; é preciso entrar nele antes
        self.frame(self.LOCATOR.GAME_IFRAME)

    def check_success(self):
        return self.get_text(self.LOCATOR.FUN_MODE) == "FUN MODE"

    def get_current_payout(self):
        return self.get_text(self.LOCATOR.CURR_PAYOUT)
