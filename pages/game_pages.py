"""Páginas do Aviator em cada cassino (URL + locators)."""
from pages.base_page import BasePage
from resources.locators import LVPageLocators, PUPageLocators


class GamePageLV(BasePage):
    """Aviator no LV Bet (página usada na coleta)."""
    URL = 'https://lvbet.com/br/slots/aviator/'
    LOCATOR = LVPageLocators


class GamePagePU(BasePage):
    """Aviator no Pin-Up Casino (alternativa; mesmas odds do LV Bet)."""
    URL = (
        'https://pin-up.casino/br/slots/spribe/aviator?lang=lang'
        '&st=8s3v0s91&s1=dte73z5u8a2wdbrvgvk0x9se9sjlpy4c&s2=2232'
        '&s3=&s4=&s5=&source=https://seawizmarine.com/&pc=30'
        '&options={options}&form_key={_form_key}'
        '&trId=cf048c1ct2hfvfk3uehg&popup={_popup}'
    )
    LOCATOR = PUPageLocators
